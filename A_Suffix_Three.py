n = int(input())
for n in range(n):
    s = input()

    if s.endswith('po'):
        print('FILIPINO')
    if s.endswith('masu') or s.endswith('desu'):
        print('JAPANESE')
    if s.endswith('mnida'):
        print('KOREAN')
    