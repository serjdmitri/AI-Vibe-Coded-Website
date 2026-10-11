import manimgx as m

NAVY = "#1E41FF"
GOLD = "#FFC906"
GREY = "#5A5F6B"


class Verstappen2023(m.Scene):
    def construct(self) -> None:
        self.camera.background_color = "#0B0F1A"

        title = m.Text("Max Verstappen", weight=m.BOLD, font_size=64)
        sub = m.Text("The 2023 Formula 1 season", font_size=34, color=GOLD)
        sub.next_to(title, m.DOWN, buff=0.4)
        self.play(m.Write(title), run_time=1.2)
        self.play(m.FadeIn(sub, shift=m.UP * 0.3))
        self.wait(1)
        self.play(m.FadeOut(title), m.FadeOut(sub))

        # 22 races: 19 wins, 3 not
        heading = m.Text("22 races. 19 wins.", font_size=48).to_edge(m.UP, buff=0.7)
        boxes = m.VGroup(
            *[m.Square(0.62, fill_opacity=1, stroke_width=0, color=GREY) for _ in range(22)]
        ).arrange_in_grid(rows=2, cols=11, buff=0.18)
        boxes.next_to(heading, m.DOWN, buff=0.8)
        self.play(m.Write(heading))
        self.play(m.LaggedStart(*[m.FadeIn(b, scale=0.5) for b in boxes], lag_ratio=0.04))
        wins = [b for i, b in enumerate(boxes) if i not in (2, 10, 21)]
        self.play(
            m.LaggedStart(*[b.animate.set_color(GOLD) for b in wins], lag_ratio=0.08),
            run_time=3,
        )
        pct = m.Text("86.4% of the season, an all-time record", font_size=32)
        pct.next_to(boxes, m.DOWN, buff=0.7)
        self.play(m.FadeIn(pct, shift=m.UP * 0.3))
        self.wait(2)
        self.play(*[m.FadeOut(x) for x in (heading, boxes, pct)])

        # Wins record vs his own 2022
        h2 = m.Text("Most wins in a season", font_size=44).to_edge(m.UP, buff=0.7)
        data = [("2022", 15, GREY), ("2023", 19, GOLD)]
        bars = m.VGroup()
        for label, val, col in data:
            bar = m.Rectangle(width=2, height=val * 0.2, fill_opacity=1, stroke_width=0, color=col)
            name = m.Text(label, font_size=30)
            num = m.Text(str(val), font_size=40, weight=m.BOLD)
            bars.add(m.VGroup(bar, name, num))
        for g, val in zip(bars, (15, 19)):
            g[1].next_to(g[0], m.DOWN, buff=0.2)
            g[2].next_to(g[0], m.UP, buff=0.2)
        bars.arrange(m.RIGHT, buff=1.6, aligned_edge=m.DOWN).shift(m.DOWN * 0.4)
        self.play(m.Write(h2))
        self.play(m.GrowFromEdge(bars[0][0], m.DOWN), m.FadeIn(bars[0][1]), m.FadeIn(bars[0][2]))
        self.play(m.GrowFromEdge(bars[1][0], m.DOWN), m.FadeIn(bars[1][1]), m.FadeIn(bars[1][2]))
        self.wait(2)
        self.play(m.FadeOut(h2), m.FadeOut(bars))

        # Points record
        h3 = m.Text("Points: 575 of a possible 620", font_size=44).to_edge(m.UP, buff=0.7)
        rows = [("Hamilton 2019", 413, GREY), ("Verstappen 2022", 454, GREY), ("Verstappen 2023", 575, GOLD)]
        group = m.VGroup()
        for label, val, col in rows:
            bar = m.Rectangle(width=val / 100, height=0.6, fill_opacity=1, stroke_width=0, color=col)
            name = m.Text(label, font_size=28)
            num = m.Text(str(val), font_size=30, weight=m.BOLD)
            line = m.VGroup(name, bar, num).arrange(m.RIGHT, buff=0.3)
            group.add(line)
        group.arrange(m.DOWN, buff=0.5, aligned_edge=m.LEFT).shift(m.DOWN * 0.3)
        self.play(m.Write(h3))
        for line in group:
            self.play(m.FadeIn(line, shift=m.RIGHT * 0.4), run_time=0.9)
        self.wait(2)
        self.play(m.FadeOut(h3), m.FadeOut(group))

        # Title
        t1 = m.Text("Champion with six races to spare", font_size=44)
        t2 = m.Text("His third straight world title", font_size=36, color=GOLD)
        t2.next_to(t1, m.DOWN, buff=0.5)
        self.play(m.Write(t1))
        self.play(m.FadeIn(t2, shift=m.UP * 0.3))
        self.wait(2.5)
        self.play(m.FadeOut(t1), m.FadeOut(t2))

        end = m.Text("4 titles: 2021, 2022, 2023, 2024", font_size=42)
        end2 = m.Text("2023 was the peak.", font_size=52, color=GOLD, weight=m.BOLD)
        end2.next_to(end, m.DOWN, buff=0.5)
        self.play(m.FadeIn(end))
        self.play(m.Write(end2))
        self.wait(2.5)
