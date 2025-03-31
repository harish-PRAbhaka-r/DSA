maxpro=0
min_p=float('inf')
for i in range(len(prices)):
  min_p=min(min_p,prices[i])
  maxpro=max(maxpro,prices[i]-min_p)
return maxpro
