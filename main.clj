(require '[clojure.string :as str])

; Utility functions

(defn hash-map-pairs [& pairs]
  (apply hash-map (flatten pairs)))

(defn twin-pair [& items]
  (for [item items] [item item]))

; Data

(def needed
  (hash-map-pairs
    (map #(for [item (str/split % #":")] (Integer/parseInt item))
      *command-line-args*)))

(def base-arrangement
  (apply hash-map-pairs
    (apply twin-pair
      (concat
        (range 1 9)
        (range 10 90 10)))))

; Transformation logic

(defn transformation-func [t]
  (fn [arrangement]
    (hash-map-pairs
      (for [piece (keys arrangement) :let [position (get arrangement piece)]]
        [piece (get t position position)]))))

(defn transformation-hash-map-from-seq [seq]
  (apply hash-map-pairs
    (for [i (-> seq count dec range)]
      [(nth seq i) (nth seq (inc i))])))

(defn transformation [key & seqs]
  (let [t (apply merge
            (for [seq seqs]
              (transformation-hash-map-from-seq seq)))]
    [key (transformation-func t)]))

(defmacro def-transformations [& ts]
  `(def transformations
    (apply hash-map-pairs
      ~@(for [tdata# ts]
        (apply transformation
          (concat [(keyword (first tdata#))] (rest tdata#)))))))

(def-transformations
  (T [3 6 5 4 3] [20 30 60 50 20])
  (B [1 8 7 2 1] [10 40 70 80 10])
  (t [1 2 4 3 1] [10 20 30 40 10])
  (b [5 6 8 7 5] [50 60 70 80 50])
  (a [1 4 2 1] [5 7 6 5] [10 40 30 10] [50 80 60 50])
  (c [1 4 2 3 1] [5 7 5] [10 30 20 40 10] [60 70 60])
  (s [1 7 3 1] [2 5 6 2] [4 8 4] [10 40 10] [20 30 20] [50 60 50] [70 80 70]))

(defn transform [ts arrangement]
  (if (empty? ts)
    arrangement
    (let [t ((last ts) transformations)]
      (t (transform (butlast ts) arrangement)))))

; From clojure-contrib.combinatorics

(defn cartesian-product
  "All the ways to take one item from each sequence"
  [& seqs]
  (let [v-original-seqs (vec seqs)
        step
        (fn step [v-seqs]
          (let [increment
                (fn [v-seqs]
                  (loop [i (dec (count v-seqs)), v-seqs v-seqs]
                    (if (= i -1) nil
                        (if-let [rst (next (v-seqs i))]
                          (assoc v-seqs i rst)
                          (recur (dec i) (assoc v-seqs i (v-original-seqs i)))))))]
            (when v-seqs
              (cons (map first v-seqs)
                    (lazy-seq (step (increment v-seqs)))))))]
    (when (every? first seqs)
      (lazy-seq (step v-original-seqs)))))

(defn selections
  "All the ways of taking n (possibly the same) elements from the sequence of items"
  [items n]
  (apply cartesian-product (take n (repeat items))))

; Create sequences of transformations

(defn transformation-sequences [& ts]
  (apply concat
    (for [i (iterate inc 1)]
      (selections ts i))))

(defn satisfies-needed [ts]
  (let [result (transform ts base-arrangement)]
    (every? true?
      (for [piece (keys needed)]
        (= (get needed piece) (get result piece))))))

(def this-one
  (first
    (drop-while #(not (satisfies-needed %))
      (apply transformation-sequences (keys transformations)))))

(println (apply str this-one))
