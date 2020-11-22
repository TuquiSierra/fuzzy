from variable import *
from membership import TriangularMembership as TriangleM, TrapezoidalMembership as TrapezoidM
from expression import AtomicExpression as Statement, AndExpression, OrExpression
from fuzzySet import FuzzySet, Term
from rule import *


forever=Term('forever', TrapezoidM(2,8,10,10))
normal=Term('normal', TrapezoidM(0, 4, 5, 10))
short=Term('short', TrapezoidM(0, 0, 3, 6))
duration=LinguisticVariable('duration', [forever, normal, short])

easy=Term('easy', TrapezoidM(0, 0, 3, 5))
medium=Term('medium',TrapezoidM(4,6,7,9))
hard=Term('hard', TrapezoidM(7, 8, 10, 10))
difficulty=LinguisticVariable('difficulty', [easy, medium, hard])

reactive=Term('reactive', TriangleM(0, 0, 4))
fifty_fifty=Term('fifty fifty', TriangleM(1,5, 9))
random=Term('random', TriangleM(6, 10, 10))
randomness=LinguisticVariable('randomness', [reactive,fifty_fifty, random])

boring=Term('boring', TriangleM(0, 0, 4))
meh=Term('fifty fifty', TriangleM(1,5, 9))
fun=Term('fun', TriangleM(6, 10, 10))
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

first_rule=Rule(long_game.And(difficult_game), boring_game)
second_rule=Rule(easy_game.Or(random_game).Or(short_game), meh_game)
third_rule=Rule(medium_game.And(like_dice).And(normal_game), fun_game)

rule_set=RuleSet([first_rule, second_rule, third_rule])

methods=[ 'bisection']
results=[]
for m in methods:
    results.append(rule_set({'duration':5, 'difficulty':8, 'randomness':2}, d_method=m))

rule_set.plot(results)



