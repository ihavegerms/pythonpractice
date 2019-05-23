'''
* Expectations
 *  - Test as you go
 *  - Solve the problem iteratively
 *  - Call out any refactors you are considering along the way and why
 *  - 
 * Scoring
 * 1 point per pin, dashes (-) are gutter balls
 * Spare ( [N, /] ): 10 points + value of next shot
 * Strike ( [X, -] ): 10 points + sum of the values of the next 2 shots
 * In the 10th frame, if the first bowl is a strike, you get 2 more rolls
 * In the 10th frame, if the second bowl is a spare, you get 1 more roll
 * The score for the 10th frame is the total number of pins knocked down in the 10th frame.
'''

import pytest

def score(rolls):

    test = []
    score = 0

    for (index, current) in enumerate(rolls):

        if index + 1 < len(rolls):
            prev = rolls[index - 1]
            current = current
            next_ = rolls[index + 1]
            if next_ == '':
                StopIteration
        if index == 9:
            prev = rolls[index - 1]
            current = current
            next_ = ''
        if index == 0:
            prev = ''
            current = current
            next_ = rolls[index +1]

        prev = [w.replace('-', '0') for w in prev]
        current = [w.replace('-', '0') for w in current]
        next_ = [w.replace('-', '0') for w in next_]
             
        pre = sum(list(map(int, prev)))
        curr = sum(list(map(int, current)))
        nex = sum(list(map(int, next_)))
        
        test.append(curr)

    return(sum(test))

  
TESTS = [
    # All numbers
    (61, [['4', '3'], ['2', '1'], ['2', '3'], ['7', '1'], ['3', '6'], ['2', '2'], ['8', '1'], ['6', '3'], ['2', '3'], ['1', '1']]),
    # dashes
    (40, [['4', '3'], ['-', '1'], ['2', '-'], ['7', '1'], ['-', '6'], ['2', '-'], ['8', '-'], ['6', '-'], ['-', '-'], ['-', '-']])
    
                                         ]
'''
    # Spares
    (69, [['4', '3'], ['9', '/'], ['2', '-'], ['7', '/'], ['-', '6'], ['2', '/'], ['8', '-'], ['6', '-'], ['-', '-'], ['-', '-']])

    # Strikes
    (87, [['X', '-'], ['2', '6'], ['X', '-'], ['7', '2'], ['X', '-'], ['-', '3'], ['X', '-'], ['-', '-'], ['3', '2'], ['1', '1']]),
    # Spares followed by Strikes
    (112, [['4', '3'], ['2', '6'], ['6', '/'], ['X', '-'], ['3', '3'], ['7', '/'], ['2', '1'], ['7', '/'], ['X', '-'], ['3', '2']]),
    # Strikes followed by Spares
    (118, [['4', '3'], ['2', '6'], ['X', '-'], ['3', '/'], ['3', '3'], ['X', '-'], ['2', '/'], ['7', '/'], ['3', '6'], ['3', '2']]),
    # Strikes followed by Strikes
    (135, [['X', '-'], ['X', '-'], ['6', '3'], ['X', '-'], ['X', '-'], ['7', '/'], ['2', '1'], ['7', '2'], ['2', '3'], ['3', '2']]),
    # Spares in last set
    (146, [['X', '-'], ['X', '-'], ['6', '3'], ['X', '-'], ['X', '-'], ['7', '/'], ['2', '1'], ['7', '2'], ['2', '3'], ['3', '/', '6']]),
    # Strikes in last set
    (149, [['X', '-'], ['X', '-'], ['6', '3'], ['X', '-'], ['X', '-'], ['7', '/'], ['2', '1'], ['7', '2'], ['2', '3'], ['X', '7', '2']]),
    # Strikes and Spares in last set
    (150, [['X', '-'], ['X', '-'], ['6', '3'], ['X', '-'], ['X', '-'], ['7', '/'], ['2', '1'], ['7', '2'], ['2', '3'], ['X', '7', '/']]),
    # All Strikes
    (300, [['X', '-'], ['X', '-'], ['X', '-'], ['X', '-'], ['X', '-'], ['X', '-'], ['X', '-'], ['X', '-'], ['X', '-'], ['X', 'X', 'X']])
        ]
'''

@pytest.mark.parametrize("expected,rolls", TESTS)
def test_scores(expected, rolls):
    assert score(rolls) == expected

pytest.main()
