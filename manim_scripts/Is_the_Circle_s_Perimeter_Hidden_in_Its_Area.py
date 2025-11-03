from manim import *

class CirclePerimeterFromArea(Scene):
    def construct(self):
        # -----------------------------
        # 0. Title
        # -----------------------------
        title = Text("Is the Circle's Perimeter Hidden in Its Area?", font_size=48)
        self.play(Write(title))
        self.wait(2)
        self.play(FadeOut(title))

        # -----------------------------
        # 1. Rajzoljunk egy kört sugárral r
        # -----------------------------
        r = 2  # alap sugár
        circle_r = Circle(radius=r, color=BLUE)
        area_formula_r = MathTex("A(r) = \\pi r^2").next_to(circle_r, DOWN)

        self.play(Create(circle_r))
        self.play(Write(area_formula_r))
        self.wait(1)

        # -----------------------------
        # 2. Rajzoljunk egy nagyobb kört r+1 sugárral
        # -----------------------------
        circle_r1 = Circle(radius=r+1, color=GREEN)
        area_formula_r1 = MathTex("A(r+1) = \\pi (r+1)^2").next_to(circle_r1, DOWN)

        self.play(Create(circle_r1))
        self.play(Write(area_formula_r1))
        self.wait(1)

        # -----------------------------
        # 3. Delta A jelölése
        # -----------------------------
        ring = Annulus(inner_radius=r, outer_radius=r+1, color=YELLOW, fill_opacity=0.2)

        arrow = Arrow(start=circle_r.get_top(), end=circle_r1.get_top(), buff=0.1, color=YELLOW)
        delta_r_text = MathTex("\\Delta r = 1").next_to(arrow, RIGHT)
        delta_A_text = MathTex("\\Delta A = A(r+1) - A(r)").next_to(arrow, DOWN, buff=0.5)

        self.play(GrowArrow(arrow))
        self.play(Write(delta_r_text))
        self.play(FadeIn(ring))
        self.wait(2)
        self.play(Write(delta_A_text))
        self.wait(2)

        # -----------------------------
        # 4. Törlés
        # -----------------------------
        self.play(FadeOut(circle_r), FadeOut(circle_r1), FadeOut(area_formula_r),
                  FadeOut(area_formula_r1), FadeOut(arrow), FadeOut(delta_r_text),
                  FadeOut(delta_A_text))
        self.wait(0.5)

        # -----------------------------
        # 5. Koordináta rendszer az A(r) függvényhez
        # -----------------------------
        axes = Axes(
            x_range=[0, 5, 1],
            y_range=[0, 20, 5],
            x_length=6,
            y_length=4,
            axis_config={"include_tip": True},
        ).to_edge(DOWN)
        x_label = axes.get_x_axis_label("r")
        y_label = axes.get_y_axis_label("A(r)")
        self.play(Create(axes), Write(x_label), Write(y_label))

        # Grafikon: A(r) = pi r^2, csak a tartomány 0-5
        def area_func(r_val):
            return np.pi * r_val**2
        graph = axes.plot(area_func, x_range=[0, 5], color=BLUE)
        self.play(Create(graph))

        # Delta vizualizáció r=2-nél
        r_val = 2
        delta_r = 1
        point1 = axes.coords_to_point(r_val, area_func(r_val))
        point2 = axes.coords_to_point(r_val+delta_r, area_func(r_val+delta_r))

        # 1. Eredeti nyíl a két pont között
        main_arrow = Arrow(start=point1, end=point2, buff=0.1, color=YELLOW)

        # 2. Függőleges nyíl ΔA-hoz
        vertical_arrow = Arrow(
            start=point1, end=axes.coords_to_point(r_val, area_func(r_val+delta_r)), buff=0.1, color=GREEN
        )
        delta_A_text = MathTex("\\Delta A = A(r+1) - A(r)").next_to(vertical_arrow, RIGHT, buff=0.7)

        # 3. Vízszintes nyíl Δr-hez
        horizontal_arrow = Arrow(
            start=point1, end=axes.coords_to_point(r_val+delta_r, area_func(r_val)), buff=0.1, color=ORANGE
        )
        delta_r_text = MathTex("\\Delta r = 1").next_to(horizontal_arrow, DOWN, buff=0.25)

        # Derivált jelzés tetején
        derivative_text = MathTex("A'(r) = \\frac{\\Delta A}{\\Delta r}").next_to(main_arrow, UP+RIGHT, buff=-0.25)

        # Animáció
        
        self.play(GrowArrow(horizontal_arrow))
        self.play(Write(delta_r_text))
        self.play(GrowArrow(vertical_arrow))
        self.play(Write(delta_A_text))
        self.wait(0.25)
        self.play(GrowArrow(main_arrow))
        self.play(Write(derivative_text))
        self.wait(2)

        # -----------------------------
        # 6. Derivált levezetése animáltan, középre
        # -----------------------------
        self.play(FadeOut(axes), FadeOut(x_label), FadeOut(y_label), FadeOut(graph),
                FadeOut(vertical_arrow), FadeOut(horizontal_arrow), FadeOut(main_arrow),
                FadeOut(delta_A_text), FadeOut(delta_r_text))
        self.wait(2)
        self.play(FadeOut(ring))#, FadeOut(derivative_text))
        frame = SurroundingRectangle(derivative_text, color=BLUE, buff=0.1)
        self.play(Create(frame))
        self.wait(0.5)

        # Képletek lépésenként
        eq1 = MathTex("A(r) = \\pi r^2")
        eq2 = MathTex("A'(r) = (\\pi r^2)'")
        eq3 = MathTex("A'(r) = \\pi (r^2)'")
        eq4 = MathTex("A'(r) = 2\\pi r")
        eq5 = MathTex("P(r) = 2r\\pi ")

        # Középre rendezés
        equations = VGroup(eq1, eq2, eq3, eq4, eq5).arrange(DOWN, center=True, buff=0.1)

        # Animált megjelenítés lépésenként
        self.play(Write(eq1))
        self.wait(0.5)
        self.play(TransformMatchingTex(eq1.copy(), eq2))
        self.wait(0.5)
        self.play(TransformMatchingTex(eq2.copy(), eq3))
        self.wait(0.5)
        self.play(TransformMatchingTex(eq3.copy(), eq4))
        self.wait(0.5)

        # Végső eredmény kiemelése és keretezése
        frame = SurroundingRectangle(eq5, color=RED, buff=0.1)
        self.play(Write(eq5))
        self.wait(0.5)
        self.play(Create(frame))
        self.wait(2)
