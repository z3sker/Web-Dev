#https://www.hackerrank.com/challenges/nested-list/problem?isFullScreen=true

if __name__ == '__main__':
    arr = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        arr.append([name, score])

    scores = sorted(set([s for _, s in arr]))
    second_lowest = scores[1]
    names = [name for name, s in arr if s == second_lowest]

    for name in sorted(names):
        print(name)