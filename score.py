
class ResultFound(Exception):
    pass

class Score:

    def __init__(self, pairs, order):
        self.top, self.bottom = self.generate_strings(pairs, order)
        if self.top == self.bottom:
            raise ResultFound('result found: {0}'.format(order))

    def generate_strings(self, pairs, order):
        return ''.join([pairs[i][0] for i in pairs]), ''.join([pairs[i][1] for i in pairs])

    def score(self):
        raise NotImplementedError()


class LongestStreak(Score):

    def score(self):
        max_streak = 0
        current_streak = 0
        for i in range(min(len(self.bottom), len(self.top))):
            if self.bottom[i] == self.top[i]:
                current_streak += 1
                max_streak = max(max_streak, current_streak)

            else:
                current_streak = 0

        return max_streak


class LongestStreakPercentage(LongestStreak):

    def score(self):
        return super().score() / min(len(self.top), len(self.bottom))


class CorrectPercentage(Score):

    def score(self):
        c = 0
        for i in range(min(len(self.top), len(self.bottom))):
            c += self.top[i] == self.bottom[i]

        return c / max(len(self.top), len(self.bottom))

    








