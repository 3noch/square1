(require '[clojure.string :as str])

(defn transformation [t]
  (fn [arrangement]
    (apply hash-map
      (flatten
        (for [piece (keys arrangement) :let [position (get arrangement piece)]]
          [piece (get t position position)])))))

(def base-arrangement {1 1, 2 2, 3 3, 4 4, 5 5, 6 6, 7 7, 8 8, 10 10, 20 20, 30 30, 40 40, 50 50, 60 60, 70 70, 80 80})

(def transformations
  {:T (transformation {3 6, 6 5, 5 4, 4 3, 20 30, 30 60, 60 50, 50 20})
   :B (transformation {1 8, 8 7, 7 2, 2 1, 10 40, 40 70, 70 80, 80 10})
   :t (transformation {1 2, 2 4, 4 3, 3 1, 10 20, 20 30, 30 40, 40 10})
   :b (transformation {5 6, 6 8, 8 7, 7 5, 50 60, 60 70, 70 80, 80 50})})

(def needed 
  (apply hash-map 
    (flatten 
      (map #(str/split % #":") *command-line-args*))))

(println ((:t transformations) base-arrangement))
