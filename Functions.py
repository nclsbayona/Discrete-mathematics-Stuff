def number_to_base(n: int, base: int):
    num=list()
    c=0
    q=base
    r=0
    while n>0:
        c=n//q
        r=n%q
        n=c
        num.insert(0,r)
    return num
    
def base_expantion(n: list, base: int):
    num=0
    total_d=len(n)
    for j in range (total_d):
        num+=(n[j]*(base**(total_d-(1+j))))
    return num

def modular_inverse(a:int, b:int):
    #MMI = lambda A, n,s=1,t=0,N=0: (n < 2 and t%N or MMI(n, A%n, t, s-A//n*t, N or n),-1)[n<1]
    for i in range(1,b):
        if ((a*i)%b==1):
            return i
        else: print(i, f"{a*i}%{b}",(a*i)%b)
    return -1
    
def chinese_remainder_theorem(congruences: list):
    x=0
    m=1
    tot=0
    M=0
    MMI = lambda A, n,s=1,t=0,N=0: (n < 2 and t%N or MMI(n, A%n, t, s-A//n*t, N or n),-1)[n<1]
    for congruence in (congruences):
        m*=int(congruence[1])
    for congruence in (congruences):
        M=m/int(congruence[1])
        print(f"{int(congruence[0])}*{M}*{MMI(M, int(congruence[1]))}",end='+')
        tot+=(int(congruence[0])*M*MMI(M, int(congruence[1])))
    x=tot
    print()
    return f"x congruent to {int(x%m)}%{m}"
    
def modular_exponentiation(b: int, n: list, m:int):
    x=1
    pw=b%m
    print (f"{base_expantion(n, 2)}=", n)
    for i in range (len(n)):
        if n[len(n)-i-1]==1:
            x=(x*pw)%m
        pw=(pw*pw)%m
        print (f"i is {i}, a_i is{n[len(n)-(i+1)]}: x is {x}, pw is {pw}")
    return f"{x}%{m}"

def euclidean_algorithm(a: int, b: int,equations=None):
    equations=equations if equations else []
    if b==0:
        return equations
    if b>a:
        a, b=b,a
    quotient=a//b
    remainder=a%b
    equations.append(f"{a}={quotient}*{b}+{remainder}")
    return euclidean_algorithm(b, remainder, equations)

def easier_gcd(a: int, b: int):
    if a<b:
        a,b=b,a
    remainder=None
    na, nb=a,b
    eucal=euclidean_algorithm(a, b)
    try:
        remainder=eucal[-2].split('+')[1]
        a=eucal[-1].split('=')[0]
        b=eucal[-1].split('*')[1].split('+')[0]
    except:
        a, b=na, nb
        remainder=nb
    return ((a,b), remainder)

def extended_euclidean_algorithm(a:int, b:int, equations=None):
    equations=equations if equations else []
    if b==0:
        return
    if a<b:
        b,a=a,b
    quotient=a//b
    remainder=a%b
    equations.append(f"1*{a}={quotient}*{b}+{remainder}")
    if extended_euclidean_algorithm(b, remainder, equations):
        return equations
    for i, equation in enumerate(equations):
        equations[i]=equation.split('+')
        equations[i][0]=equations[i][0].split('=')
        equations[i][0]="-".join(equations[i][0])
        equations[i]='='.join(equations[i])
    return True

def caesar_cypher(word:str, k: int, a: int):
    alphabeth=list("a b c d e f g h i j k l m n o p q r s t u v w x y z".split())
    word=list(word)
    new_word=[]
    for letter in (word):
        if letter==' ':
            new_word.append(' ')
            continue
        new_word.append(alphabeth[(a*(alphabeth.index(letter.lower())+k))%len(alphabeth)])
    return ''.join(new_word)

def primitive_root(num, mod):
    x=list()
    for i in range(1, mod):
        x.append(f"{num**i}%{mod}={modular_exponentiation(num, number_to_base(i, 2), mod)}")
    print(x)

def main(args):
    #MMI = lambda A, n,s=1,t=0,N=0: (n < 2 and t%N or MMI(n, A%n, t, s-A//n*t, N or n),-1)[n<1]
    option=input("Start? (y/n) ")
    while option.lower()=="y":
        print (1, "Easier gcd")
        print (2, "Number to base")
        print (3, "Base expantion")
        print (4, "Modular exponentiation")
        print (5, "Normal euclidean algorithm")
        print (6, "Extended euclidean algorithm")
        print (7, "Modular inverse")
        print(8, "Solver")
        print (9, "Chinese remainder theorem")
        print (10, "Caesar cypher")
        print (11, "Primitive root")
        option=int(input())
        if option==1:
            print("First number:", end=' ')
            a=int(input())
            print("Second number:", end=' ')
            b=int(input())
            print (easier_gcd(a,b))
        elif option==2:
            print("Number in base 10:", end=' ')
            a=int(input())
            print("Desired base:", end=' ')
            b=int(input())
            print (number_to_base(a,b))
        elif option==3:
            print("Input number (Separated by spaces)")
            lst=input().split(' ')
            lst=list(map(int, lst))
            print ("Base: ", end='')
            bse=int(input())
            print(base_expantion(lst, bse))
        elif option==4:
            print("Number in base 10:", end=' ')
            a=int(input())
            baseC=input("Dont have list? (do)")
            if baseC.lower()=="do":
                print ("Number: ",end='')
                number=int(input())
                lst=number_to_base(number, 2)
            else:
                lst=list(map(int,list(input("List chars separated by spaces: ").split(' '))))
            print("Modulo:", end=' ')
            b=int(input())
            print (modular_exponentiation(a, lst,b))
        elif option==5:
            print("First number:", end=' ')
            a=int(input())
            print("Second number:", end=' ')
            b=int(input())
            print (euclidean_algorithm(a,b))
        elif option==6:
            print("First number:", end=' ')
            a=int(input())
            print("Second number:", end=' ')
            b=int(input())
            print (extended_euclidean_algorithm(a,b))
        elif option==7:
            print("Number: ", end=' ')
            a=int(input())
            print("Modulo: ", end=' ')
            b=int(input())
            try:
                x=modular_inverse(a,b)
                if x<1:
                    raise Exception
                print(x)
            except:
                print("Does not exist")
        elif option==8:
            print(eval(input()))
        elif option==9:
            congruence=None
            congruences=list()
            n=int(input("Number of congruences: "))
            for i in range(n):
                congruence=(input(f"Congruence {i+1}: ").split('%'))
                congruences.append(congruence)
                congruence=None
            print (chinese_remainder_theorem(congruences))
        elif option==10:
            word=input("Word: ")
            n=int(input("k: "))
            na=int(input("a: "))
            print(caesar_cypher(word, n, na))
        elif option==11:
            num=int(input("Number"))
            mod=int(input("Modulo"))
            primitive_root(num, mod)
        
        option=input("Again? (y/n) ")
    return 0

if __name__ == '__main__':
    from sys import argv
    main(argv)
