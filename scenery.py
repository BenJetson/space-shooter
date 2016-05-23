import random

from assets import *

class Stars:

    def __init__(self, x, y, w, h, num_stars):
        self.stars = []

        for n in range(num_stars):
            a = random.randrange(x, x + w)
            b = random.randrange(y, y + h)

            self.stars.append([a, b])

    def update(self):
        for s in self.stars:
            s[1] += 0.25

            if s[1] > 560:
                s[0] = random.randrange(0, 1000)
                s[1] = random.randrange(-25, 0)

    def draw(self, screen):
        for s in self.stars:
            pygame.draw.ellipse(screen, WHITE, [s[0], s[1], 1, 1])


class Mountains:

    def __init__(self, x, y, w, h, num_peaks):
        self.peaks = []

        self.peaks.append([x, y + h])
        self.peaks.append([x, y + 4 * h // 5])

        for n in range(1, num_peaks):
            center = n * w // num_peaks
            offset = w // num_peaks // 4

            a = random.randrange(center - offset, center + offset)
            b = random.randrange(y, y + 4 * h // 5)

            self.peaks.append([a, b])

        self.peaks.append([x + w, y + 4 * h // 5])
        self.peaks.append([x + w, y + h])


    def draw(self, screen):
        pygame.draw.polygon(screen, LIGHT_GREY, self.peaks)
