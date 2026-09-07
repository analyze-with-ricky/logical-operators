# +-----+-----+-----+
#  LOGICAL OPERATORS                   
# +-----+-----+-----+

class Operators:
    def conjunction(self):
        print("\n+-----+-----+-----+-----+")
        print("CONJUNCTION TRUTH TABLE")
        print("+-----+-----+-----+-----+")
        print()
        print("+-----+-----+---------+")
        print("|  T  |  T  |    T    |")
        print("+-----+-----+---------+")
        print("|  T  |  F  |    F    |")
        print("+-----+-----+---------+")
        print("|  F  |  T  |    F    |")
        print("+-----+-----+---------+")
        print("|  F  |  F  |    F    |")
        print("+-----+-----+---------+")
        print()
        
    def disjunction(self):
        print("\n+-----+-----+-----+-----+")
        print("DISJUNCTION TRUTH TABLE")
        print("+-----+-----+-----+-----+")
        print()
        print("+-----+-----+---------+")
        print("|  T  |  T  |    T    |")
        print("+-----+-----+---------+")
        print("|  T  |  F  |    T    |")
        print("+-----+-----+---------+")
        print("|  F  |  T  |    T    |")
        print("+-----+-----+---------+")
        print("|  F  |  F  |    F    |")
        print("+-----+-----+---------+")
        print()

    def negation(self):
        print("\n+-----+-----+-----+-----+")
        print("NEGATION TRUTH TABLE")
        print("+-----+-----+-----+-----+")
        print()
        print("+-----+-----+")
        print("|  T  |  F  |")
        print("+-----+-----+")
        print("|  F  |  T  |")
        print("+-----+-----+")
        print()

    def exclusiveOR(self):
        print("\n+-----+-----+-----+-----+")
        print("EXCLUSIVE OR TRUTH TABLE")
        print("+-----+-----+-----+-----+")
        print()
        print("+-----+-----+---------+")
        print("|  T  |  T  |    F    |")
        print("+-----+-----+---------+")
        print("|  T  |  F  |    T    |")
        print("+-----+-----+---------+")
        print("|  F  |  T  |    T    |")
        print("+-----+-----+---------+")
        print("|  F  |  F  |    F    |")
        print("+-----+-----+---------+")
        print()

    def implication(self):
        print("\n+-----+-----+-----+-----+")
        print("IMPLICATION TRUTH TABLE")
        print("+-----+-----+-----+-----+")
        print()
        print("+-----+-----+---------+")
        print("|  T  |  T  |    T    |")
        print("+-----+-----+---------+")
        print("|  T  |  F  |    F    |")
        print("+-----+-----+---------+")
        print("|  F  |  T  |    T    |")
        print("+-----+-----+---------+")
        print("|  F  |  F  |    T    |")
        print("+-----+-----+---------+")
        print()

    def biconditional(self):
        print("\n+-----+-----+-----+-----+")
        print("BICONDITIONAL TRUTH TABLE")
        print("+-----+-----+-----+-----+")
        print()
        print("+-----+-----+---------+")
        print("|  T  |  T  |    T    |")
        print("+-----+-----+---------+")
        print("|  T  |  F  |    F    |")
        print("+-----+-----+---------+")
        print("|  F  |  T  |    F    |")
        print("+-----+-----+---------+")
        print("|  F  |  F  |    T    |")
        print("+-----+-----+---------+")
        print()


obj_operators = Operators()
print("----+----+----+----")
print("LOGICAL OPERATORS")
print("----+----+----+----")
print("1) Conjunction\n2) Disjunction\n3) Negation\n4) Exclusive OR\n5) Implication\n6) Biconditional")
user_input = input("Enter your choice(1, 2, 3, 4, 5, & 6): ")

if user_input == "1":
    obj_operators.conjunction()
elif user_input == "2":
    obj_operators.disjunction()
elif user_input == "3":
    obj_operators.negation()
elif user_input == "4":
    obj_operators.exclusiveOR()
elif user_input == "5":
    obj_operators.implication()
elif user_input == "6":
    obj_operators.biconditional()
else:
    print("Invalid Choice!")


