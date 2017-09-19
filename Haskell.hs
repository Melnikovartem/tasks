import qualified Data.Set as Set
set x = Set.toList $ Set.fromList x
line x = 1 == (length $ set x)
result x = if length x == 1 then head $ head x else 'D'
answer input = result $ filter line $ input ++ [[x!!num| x <- input]|num<-[0..2]] ++ [[input!!n!!n|n<-[0..2]]] ++ [[input!!n!!(2-n)|n<-[0..2]]]

test = [
    ([
    "X.O",
    "XX.",
    "XOO"], 'X'),
    (["OO.",
    "XOX",
    "XOX"], 'O'),
    ([
    "OO.",
    "XOX",
    "XOX"], 'O'),
    ([
    "XO.",
    "OX.",
    "OOX"], 'X'),
    ([
    "OOX",
    "OX.",
    "XO."], 'X'),
    ([
    "OOX",
    "OXX",
    "OXX"], 'D'),
    ([
    "X.O",
    "O.X",
    "O.X"], '.')
    ]

check x = (answer $ fst x) == (snd x)
test_it = foldr (&&) True $ map check test  	
