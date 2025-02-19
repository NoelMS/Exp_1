def pattern(l):
    for i in l:
        print(i*'*')
def main():
    l=[]
    n=input("Enter number of lines: ")
    for i in n:
        l.append(input('Enter number of * to print: '))
    pattern(l)
main()