import System (getArgs)

type Mapping = [(Int,Int)]
type Move = Int -> Int
type Path = [Transform]
data Transform = Transform { name :: String
                           , move :: Move
                           }


instance Show Transform where
    show (Transform name _) = show name


main :: IO ()
main = do
    args <- getArgs
    let goal = read (args !! 0) :: Mapping
    putStrLn $ show (find goal)

pathsOfLen :: Int -> [Path]
pathsOfLen n = sequence (replicate n transformations)

transform :: Path -> Move
transform []     = (\a -> a)
transform (x:xs) = move x . transform xs

filterMoves :: Int -> Int -> [Path] -> [Path]
filterMoves start end = filter (\x -> transform x start == end)

reach' :: Mapping -> [Path] -> [Path]
reach' [] _ = concat [pathsOfLen n | n <- [1..]]
reach' (x:xs) pool = filterMoves (fst x) (snd x) (reach' xs pool)

reach :: Mapping -> [Path]
reach x = reach' x (reach' [] [])

find :: Mapping -> Path
find x = head $ reach x




transformations = [ Transform "T" t'
                  , Transform "B" b'
                  , Transform "t" t
                  , Transform "b" b
                  , Transform "a" a
                  , Transform "c" c
                  , Transform "s" s
                  , Transform "c b c b^-1 c" cbcbc
                  , Transform "T^2 B^2" tb'
                  ]


t' :: Move
t'  3 =  6
t'  4 =  3
t'  5 =  4
t'  6 =  5
t' 20 = 30
t' 30 = 60
t' 50 = 20
t' 60 = 50
t'  x =  x

b' :: Move
b'  1 =  8
b'  2 =  1
b'  7 =  2
b'  8 =  7
b' 10 = 40
b' 40 = 70
b' 70 = 80
b' 80 = 10
b'  x =  x

t :: Move
t  1 =  2
t  2 =  4
t  3 =  1
t  4 =  3
t 10 = 20
t 20 = 30
t 30 = 40
t 40 = 10
t  x =  x

b :: Move
b  5 =  6
b  6 =  8
b  7 =  5
b  8 =  7
b 50 = 60
b 60 = 70
b 70 = 80
b 80 = 50
b  x =  x

a :: Move
a  1 =  4
a  2 =  1
a  4 =  2
a  5 =  7
a  6 =  5
a  7 =  6
a 10 = 40
a 30 = 10
a 40 = 30
a 50 = 80
a 60 = 50
a 80 = 60
a  x =  x

c :: Move
c  1 =  4
c  2 =  3
c  3 =  1
c  4 =  2
c  5 =  7
c  7 =  5
c 10 = 30
c 20 = 40
c 30 = 20
c 40 = 10
c 60 = 70
c 70 = 60
c  x =  x

s :: Move
s  1 =  7
s  2 =  5
s  3 =  1
s  4 =  8
s  5 =  6
s  6 =  2
s  7 =  3
s  8 =  4
s 10 = 40
s 20 = 30
s 30 = 20
s 40 = 10
s 50 = 60
s 60 = 50
s 70 = 80
s 80 = 70
s  x =  x

cbcbc :: Move
cbcbc  1 =  3
cbcbc  2 =  4
cbcbc  3 =  2
cbcbc  4 =  1
cbcbc  5 =  8
cbcbc  8 =  5
cbcbc 10 = 40
cbcbc 20 = 30
cbcbc 30 = 10
cbcbc 40 = 20
cbcbc 50 = 70
cbcbc 70 = 50
cbcbc  x =  x

tb' :: Move
tb'  1 =  7
tb'  2 =  8
tb'  3 =  5
tb'  4 =  6
tb'  5 =  3
tb'  6 =  4
tb'  7 =  1
tb'  8 =  2
tb' 10 = 70
tb' 20 = 60
tb' 30 = 50
tb' 40 = 80
tb' 50 = 30
tb' 60 = 20
tb' 70 = 10
tb' 80 = 40
tb'  x =  x
