# state defined as (on 1st, on 2nd, on 3rd, inning, outs, score)

def walk(state):
    # no one on first
    if not state[0]:
        return (True, state[1], state[2], state[3], state[4], state[5])
    # no one on second
    elif not state[1]:
        return (True, True, state[2], state[3], state[4], state[5])
    # no one on third
    elif not state[2]:
        return (True, True, True, state[3], state[4], state[5])
    # someone on every base
    else:
        return (True, True, True, state[3], state[4], state[5]+1)

def strikeout(state):
    # 2 outs
    if state[4] == 2:
        # not last inning
        if state[3] < 7:
            return (False, False, False, state[3]+1, 0, state[5])
        else:
            # end of game
            return
    else:
        return (state[0], state[1], state[2], state[3], state[4]+1, state[5])

def single(state):
    score = state[5]
    # People on 2nd and 3rd score
    if state[1]:
        score += 1
    if state[2]:
        score += 1
    # if someone on 1st --> 3rd
    if state[0]:
        return (True, False, True, state[3], state[4], score)
    else:
        return (True, False, False, state[3], state[4], score)

def double(state):
    score = state[5]
    # People on 1st, 2nd, and 3rd score
    if state[0]:
        score += 1
    if state[1]:
        score += 1
    if state[2]:
        score += 1
    return (False, True, False, state[3], state[4], score)

def triple(state):
    score = state[5]
    # People on 1st, 2nd, and 3rd score
    if state[0]:
        score += 1
    if state[1]:
        score += 1
    if state[2]:
        score += 1
    return (False, False, True, state[3], state[4], score)

def homerun(state):
    # batter scores
    score = state[5] + 1
    # People on 1st, 2nd, and 3rd score
    if state[0]:
        score += 1
    if state[1]:
        score += 1
    if state[2]:
        score += 1
    return (False, False, False, state[3], state[4], score)

# TODO: based on answers to chat
def out_advance_runners(state):
    if state[4] == 2:
        # not last inning
        if state[3] < 7:
            return (False, False, False, state[3]+1, 0, state[5])
        else:
            # end of game
            return
    else:
        score = state[5]
        # person on 3rd scores
        if state[2]:
            score += 1
        # everyone goes forward one
        return (False, state[0], state[1], state[3], state[4]+1, state[5])

def out_no_advance(state):
    # if already 2 outs
    if state[4] == 2:
        # not last inning
        if state[3] < 7:
            return (False, False, False, state[3]+1, 0, state[5])
        else:
            # end of game
            return
    else:
        return (state[0], state[1], state[2], state[3], state[4]+1, state[5])
