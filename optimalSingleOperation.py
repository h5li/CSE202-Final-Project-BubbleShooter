from reachable import reachable
def findTheOptimalShot(M,listOfBubbles): 
    maxScore = 0
    for bubble in listOfBubbles:
        maxScore = max(maxScore,findTheMaxScoreForOneShot(M,bubble))
    return maxScore

def findTheMaxScoreForOneShot(M, bubble): 
    availablePositions = reachable(M) 
    maxScore = 0
    for pos in availablePositions:
        removed_balls,locs_to_delete = BubblesPoppedDFS(M, pos, bubble)
        maxScore = max(maxScore,calculateScore(removed_balls))
    return maxScore

def calculateScore(numBalls):
    if numBalls <= 3:
        return numBalls * 10
    else:
        return (1+numBalls-3)*numBalls*10/2 + 30
