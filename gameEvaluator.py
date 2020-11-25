from variable import *
from membership import TriangularMembership as TriangleM, TrapezoidalMembership as TrapezoidM, SigmoidalMembership as Sigmoid
from expression import AtomicExpression as Statement, AndExpression, OrExpression
from fuzzySet import FuzzySet
from rule import *

forever=Adjective('forever', TrapezoidM(0,0,2,4))
normal=Adjective('normal', TrapezoidM(3, 5, 7, 8))
short=Adjective('short', TrapezoidM(7, 8, 10, 10))
duration=LinguisticVariable('duration', [forever, normal, short])


easy=Adjective('easy', TrapezoidM(0, 0, 3, 5))
medium=Adjective('medium',TrapezoidM(4,6,7,9))
hard=Adjective('hard', TrapezoidM(7, 8, 10, 10))
difficulty=LinguisticVariable('difficulty', [easy, medium, hard])

reactive=Adjective('reactive', TriangleM(0, 0, 4))
fifty_fifty=Adjective('fifty fifty', TriangleM(1,5, 9))
random=Adjective('random', TriangleM(6, 10, 10))
randomness=LinguisticVariable('randomness', [reactive,fifty_fifty, random])

boring=Adjective('boring', TrapezoidM(0, 0,3, 4))
meh=Adjective('fifty fifty', TrapezoidM(3,4, 7, 8))
fun=Adjective('fun', TrapezoidM(7, 8, 10, 10))
classification=LinguisticVariable('classification', [boring,meh, fun])

difficult_game=Statement(difficulty, hard)
medium_game=Statement(difficulty, medium)
easy_game=Statement(difficulty, easy)

random_game=Statement(randomness, random)
like_dice=Statement(randomness, fifty_fifty)
reactive=Statement(randomness, reactive)

long_game=Statement(duration, forever)
normal_game=Statement(duration, normal)
short_game=Statement(duration, short)

boring_game=Statement(classification, boring)
meh_game=Statement(classification, meh)
fun_game=Statement(classification, fun)

first_rule=Rule(long_game.Or(easy_game), boring_game)
second_rule=Rule(normal_game, meh_game)
third_rule=Rule(short_game.Or(difficult_game), fun_game)

rule_set=RuleSet([first_rule, second_rule, third_rule])

