allWeight = int(input())
bothCost = int(input())
costFirst = int(input())
costSecond = int(input())

weightFist = int((allWeight * bothCost - costSecond * allWeight) / (costFirst - costSecond))
weightSecond = int(allWeight - weightFist)

print(f"{weightFist} {weightSecond}")
