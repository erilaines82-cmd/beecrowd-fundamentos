N = int(input())

print(N)

for nota in [100, 50, 20, 10, 5, 2, 1]:
    quantidade = N // nota
    N = N % nota
    print(f"{quantidade} nota(s) de R$ {nota},00")
