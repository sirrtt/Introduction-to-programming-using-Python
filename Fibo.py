def fibo(n):
    if n <= 1:
        return n
    else:
        return(fibo(n-1) + fibo(n-2))

def main():
    n = int(input())
    if n<1 or n>30:
        print(f'So {n} khong nam trong khoang [1,30].')
    else:
        print(fibo(n))

main()

