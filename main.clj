(require '[clojure.string :as str])

; Utility functions

(defn hash-map-pairs [& pairs]
  (apply hash-map (flatten pairs)))

(defn twin-pair [& items]
  (for [item items] [item item]))

; Data

(def needed
  (hash-map-pairs
    (map #(str/split % #":") *command-line-args*)))

(def base-arrangement
  (apply hash-map-pairs
    (apply twin-pair
      (concat
        (range 1 9)
        (range 10 90 10)))))

; Core logic

(defn transformation-func [t]
  (fn [arrangement]
    (hash-map-pairs
      (for [piece (keys arrangement) :let [position (get arrangement piece)]]
        [piece (get t position position)]))))

(defn transformation-hash-map-from-seq [seq]
  (apply hash-map-pairs
    (for [i (-> seq count dec range) :let [j (inc i)]] 
      [(nth seq i) (nth seq j)])))

(defn transformation [key & seqs]
  (let [t (apply merge
            (for [seq seqs] (transformation-hash-map-from-seq seq)))]
    [key (transformation-func t)]))

(def transformations
  (hash-map-pairs
    (transformation :T [3 6 5 4 3] [20 30 60 50 20])
    (transformation :B [1 8 7 2 1] [10 40 70 80 10])
    (transformation :t [1 2 4 3 1] [10 20 30 40 10])
    (transformation :b [5 6 8 7 5] [50 60 70 80 50])))

(println ((:t transformations) base-arrangement))
