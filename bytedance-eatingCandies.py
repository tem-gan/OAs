#https://codeforces.com/problemset/problem/1669/F
def eatingCandies(candies):
  
  for idx in range(len(candies):
    l = 0
    r = len(candies) - 1
    suml = candies[0]
    sumr = candies[len(candies)-1]
    ans = 0
    while l < r:
        if suml == sumr:
            ans = max(ans, l + 1 + n - r)

        if suml <= sumr:
            l+=1
            suml+=candies[l]

        elif sumr < suml:
            r-=1
            sumr+=candies[r]
            
    return ans
