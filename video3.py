from manim import *

class Ecuacion(Scene):
    def construct(self):
        ec = MathTex(r"b^n mod \thinspace k").scale(3)
        self.play(Write(ec),runtime=5)
        self.wait(5)
        self.play(FadeOut(ec))

class Escena(Scene):
    def construct(self):
        expr = MathTex(r"b^n")
        bin_expr = MathTex(r"bin(n)")
        mov_bin = MathTex(r"bin(n)")
        equals = MathTex(r"=")
        pol = MathTex(r"a_m*2^m+a_{m-1}*2^{m-1}+ \dotsc +a_1*2^1+a_0*2^0")

        expr.move_to(ORIGIN)
        bin_expr.move_to(ORIGIN)
        VGroup(mov_bin, equals, pol).arrange(RIGHT)

        self.play(Write(expr), runtime=3)
        self.play(expr.animate.shift(UP*2))
        self.wait(1)
        self.play(FadeIn(bin_expr))
        self.wait(2)
        self.play(Transform(bin_expr, mov_bin),FadeIn(equals),FadeIn(pol))
        self.wait(2)

        expr2 = MathTex(r"b^n")
        equals3 = MathTex(r"=")
        pol2 = MathTex(r"b^{a_m*2^m+a_{m-1}*2^{m-1}+ \dotsc +a_1*2^1+a_0*2^0}")

        VGroup(expr2, equals3, pol2).arrange(RIGHT).move_to(UP*2)

        self.play(Transform(expr, expr2), FadeIn(equals3), FadeIn(pol2))
        self.wait(2)

        pol3 = MathTex(r"b^{a_m*2^m}b^{a_{m-1}*2^{m-1}} \dotsc b^{a_1*2^1}b^{a_0*2^0}")
        pol3.next_to(pol2,DOWN*0.7)

        self.play(Write(pol3))
        self.wait(2)

        bin_num = MathTex(r"bin(75)")
        equals2 = MathTex(r"=")
        num_pol = MathTex(r"1 ~ 0 ~ 0 ~ 1 ~ 0 ~ 1 ~ 1")

        VGroup(bin_num, equals2, num_pol).arrange(RIGHT)

        self.play(Transform(bin_expr, bin_num),Transform(equals, equals2),Transform(pol, num_pol))
        self.wait(1)

        expr_ej = MathTex(r"b^{75}")
        equals4 = MathTex(r"=")
        pol4 = MathTex(r"b^{1000000}b^{1000}b^{10}b")
        VGroup(expr_ej, equals4, pol4).arrange(RIGHT).move_to(UP*2)
        self.play(Transform(expr, expr_ej), Transform(equals3, equals4), Transform(pol3, pol4), FadeOut(pol2))
        self.wait(2)
        self.play(
            FadeOut(bin_expr),
            FadeOut(equals),
            FadeOut(pol),
            FadeOut(expr),
            FadeOut(equals3),
            FadeOut(pol3)
        )

class Escena2(Scene):
    def construct(self):
        line = Line([-8, 0.8, 0], [8, 0.8, 0])
        line2 = Line([-8, 2.2, 0], [8, 2.2, 0])
        square = Square(stroke_color=YELLOW, fill_opacity=0, stroke_opacity=2, stroke_width=10).scale(0.75).move_to(UP*1.5)
        bin_digits = MathTex(r"1 ~","~ 0 ~","~ 0 ~","~ 1 ~","~ 0 ~","~ 1 ~","~ 1").move_to(UP*1.5).scale(2)
        bin_digits.next_to(bin_digits[6],ORIGIN)
        var = MathTex(r"r").move_to(LEFT + DOWN).scale(2.5)
        self.play(FadeIn(bin_digits),FadeIn(var),Create(line),Create(line2))
        self.play(Create(square))
        self.wait(2)
        mov_var = MathTex(r"r").move_to(LEFT * 4 + DOWN).scale(2.5)
        equals = MathTex(r"~ =").next_to(mov_var,RIGHT*2).scale(2.5)
        value = MathTex(r"1").move_to(DOWN).scale(3)
        self.play(Transform(var, mov_var) ,FadeIn(equals), FadeIn(value))
        self.wait(2)
        instruction = MathTex(r"if~ bit == 1:~ r = b*r").move_to(UP*3)
        value1 = MathTex(r"1*b").move_to(DOWN).scale(3)
        value2 = MathTex(r"b").move_to(DOWN).scale(3)
        self.play(FadeIn(instruction))
        self.play(Transform(value, value1))
        self.wait(1)
        self.play(Transform(value, value2))
        self.wait(2)
        instruction2 = MathTex(r"r = r^2").move_to(UP * 3.8)
        value3 = MathTex(r"b^2").move_to(DOWN).scale(3)
        self.play(bin_digits.animate.next_to(bin_digits[2],ORIGIN))
        self.play(FadeIn(instruction2))
        self.wait(1)
        self.play(Transform(value, value3))
        self.wait(2)
        value4 = MathTex(r"(b^2)^2").move_to(DOWN).scale(3)
        value5 = MathTex(r"b^4").move_to(DOWN).scale(3)
        self.play(bin_digits.animate.next_to(bin_digits[2], ORIGIN))
        self.wait(1)
        self.play(Transform(value, value4))
        self.wait(1)
        self.play(Transform(value, value5))
        self.wait(2)
        value6 = MathTex(r"(b^4)^2").move_to(DOWN).scale(3)
        value7 = MathTex(r"b^8").move_to(DOWN).scale(3)
        value8 = MathTex(r"b^8*b").move_to(DOWN).scale(3)
        value9 = MathTex(r"b^9").move_to(DOWN).scale(3)
        self.play(bin_digits.animate.next_to(bin_digits[2], ORIGIN))
        self.wait(1)
        self.play(Transform(value, value6))
        self.wait(1)
        self.play(Transform(value, value7))
        self.wait(1)
        self.play(Transform(value, value8))
        self.wait(1)
        self.play(Transform(value, value9))
        self.wait(2)
        value10 = MathTex(r"(b^9)^2").move_to(DOWN).scale(3)
        value11 = MathTex(r"b^{18}").move_to(DOWN).scale(3)
        self.play(bin_digits.animate.next_to(bin_digits[2], ORIGIN))
        self.wait(1)
        self.play(Transform(value, value10))
        self.wait(1)
        self.play(Transform(value, value11))
        self.wait(2)
        value12 = MathTex(r"(b^{18})^2").move_to(DOWN).scale(3)
        value13 = MathTex(r"b^{36}").move_to(DOWN).scale(3)
        value14 = MathTex(r"b^{36}*b").move_to(DOWN).scale(3)
        value15 = MathTex(r"b^{37}").move_to(DOWN).scale(3)
        self.play(bin_digits.animate.next_to(bin_digits[2], ORIGIN))
        self.wait(1)
        self.play(Transform(value, value12))
        self.wait(1)
        self.play(Transform(value, value13))
        self.wait(1)
        self.play(Transform(value, value14))
        self.wait(1)
        self.play(Transform(value, value15))
        self.wait(2)
        value16 = MathTex(r"(b^{37})^2").move_to(DOWN).scale(3)
        value17 = MathTex(r"b^{74}").move_to(DOWN).scale(3)
        value18 = MathTex(r"b^{74}*b").move_to(DOWN).scale(3)
        value19 = MathTex(r"b^{75}").move_to(DOWN).scale(3)
        self.play(bin_digits.animate.next_to(bin_digits[2], ORIGIN))
        self.wait(1)
        self.play(Transform(value, value16))
        self.wait(1)
        self.play(Transform(value, value17))
        self.wait(1)
        self.play(Transform(value, value18))
        self.wait(1)
        self.play(Transform(value, value19))
        self.wait(4)
        self.play(
            FadeOut(line),
            FadeOut(line2),
            FadeOut(square),
            FadeOut(bin_digits),
            FadeOut(var),
            FadeOut(equals),
            FadeOut(value),
            FadeOut(instruction),
            FadeOut(instruction2)
        )

class Escena3(Scene):
    def construct(self):
        var = MathTex(r"S")
        equals = MathTex(r"=")
        expr = MathTex(r"\sum_{k=0}^{\infty}\frac{p(k)}{b^{ck}q(k)}")
        VGroup(var, equals, expr).arrange(RIGHT)
        self.play(Write(var),Write(equals),Write(expr))
        self.wait(2)
        var1 = MathTex(r"b^nS")
        equals1 = MathTex(r"=")
        expr1 = MathTex(r"\sum_{k=0}^{\infty}\frac{b^np(k)}{b^{ck}q(k)}")
        VGroup(var1, equals1, expr1).arrange(RIGHT)
        self.play(Transform(var,var1),Transform(equals,equals1),Transform(expr,expr1))
        self.wait(2)
        var2 = MathTex(r"b^nS")
        equals2 = MathTex(r"=")
        expr2 = MathTex(r"\sum_{k=0}^{\infty}\frac{b^{n-ck}p(k)}{q(k)}")
        VGroup(var2, equals2, expr2).arrange(RIGHT)
        self.play(Transform(var,var2),Transform(equals,equals2),Transform(expr,expr2))
        self.wait(2)
        var3 = MathTex(r"b^nS")
        varmod3 = MathTex(r"mod ~ 1")
        equals3 = MathTex(r"=")
        expr3 = MathTex(r"\sum_{k=0}^{\infty}\frac{b^{n-ck}p(k)}{q(k)}")
        exprmod3 = MathTex(r"mod ~ 1")
        VGroup(var3, varmod3, equals3, expr3, exprmod3).arrange(RIGHT)
        self.play(
            Transform(var, var3),
            FadeIn(varmod3),
            Transform(equals, equals3),
            Transform(expr, expr3),
            FadeIn(exprmod3)
        )
        self.wait(2)
        var4 = MathTex(r"b^nS")
        varmod4 = MathTex(r"mod ~ 1")
        equals4 = MathTex(r"=")
        expr4_1 = MathTex(r"\sum_{k=0}^{\lfloor\frac{n}{c}\rfloor}\frac{b^{n-ck}p(k)}{q(k)}")
        exprmod4_1 = MathTex(r"mod ~ 1")
        sum4 = MathTex(r"+")
        expr4_2 = MathTex(r"\sum_{k=\lfloor\frac{n}{c}\rfloor+1}^{\infty}\frac{b^{n-ck}p(k)}{q(k)}")
        exprmod4_2 = MathTex(r"mod ~ 1")
        VGroup(var4, varmod4, equals4, expr4_1, exprmod4_1).arrange(RIGHT)
        VGroup(sum4, expr4_2, exprmod4_2).arrange(RIGHT).next_to(expr4_1,DOWN*2)
        self.play(
            Transform(var, var4),
            Transform(varmod3, varmod4),
            Transform(equals, equals4),
            Transform(expr, expr4_1),
            Transform(exprmod3,exprmod4_1),
            FadeIn(sum4),
            FadeIn(expr4_2),
            FadeIn(exprmod4_2),
        )
        self.wait(2)
        var5 = MathTex(r"b^nS")
        varmod5 = MathTex(r"mod ~ 1")
        equals5 = MathTex(r"=")
        expr5_1 = MathTex(r"\sum_{k=0}^{\lfloor\frac{n}{c}\rfloor}\frac{b^{n-ck}p(k)~mod ~ q(k)}{q(k)}")
        exprmod5_1 = MathTex(r"mod ~ 1")
        sum5 = MathTex(r"+")
        expr5_2 = MathTex(r"\sum_{k=\lfloor\frac{n}{c}\rfloor+1}^{\infty}\frac{b^{n-ck}p(k)}{q(k)}")
        exprmod5_2 = MathTex(r"mod ~ 1")
        VGroup(var5, varmod5, equals5, expr5_1, exprmod5_1).arrange(RIGHT)
        VGroup(sum5, expr5_2, exprmod5_2).arrange(RIGHT).next_to(expr5_1, DOWN*2)
        self.play(
            Transform(var, var5),
            Transform(varmod3, varmod5),
            Transform(equals, equals5),
            Transform(expr, expr5_1),
            Transform(exprmod3, exprmod5_1),
            Transform(sum4, sum5),
            Transform(expr4_2, expr5_2),
            Transform(exprmod4_2, exprmod5_2)
        )
        self.wait(4)

class Escena4(Scene):
    def construct(self):
        var = MathTex(r"b^dS")
        varmod = MathTex(r"mod ~ 1")
        equals = MathTex(r"=")
        expr_1 = MathTex(r"\sum_{k=0}^{\lfloor\frac{d}{c}\rfloor}\frac{b^{d-ck}mod ~ q(k) \cdot p(k)~mod ~ q(k)}{q(k)}")
        exprmod_1 = MathTex(r"mod ~ 1")
        sum = MathTex(r"+")
        expr_2 = MathTex(r"\sum_{k=\lfloor\frac{d}{c}\rfloor+1}^{\infty}\frac{b^{d-ck}p(k)}{q(k)}")
        exprmod_2 = MathTex(r"mod ~ 1")
        VGroup(var, varmod, equals, expr_1, exprmod_1).arrange(RIGHT)
        VGroup(sum, expr_2, exprmod_2).arrange(RIGHT).next_to(expr_1, DOWN * 2)
        self.play(
            FadeIn(var),
            FadeIn(varmod),
            FadeIn(equals),
            FadeIn(expr_1),
            FadeIn(exprmod_1),
            FadeIn(sum),
            FadeIn(expr_2),
            FadeIn(exprmod_2)
        )
        self.wait(4)
        log = MathTex(r"Log(2)")
        pi = MathTex(r"\pi")
        logsqr = MathTex(r"Log(2)^2")
        pisqr = MathTex(r"\pi^2")
        olog = MathTex(r"Log(9/10)")
        VGroup(log, pi, logsqr, pisqr, olog).arrange(RIGHT*3.5).move_to(UP*3).scale(1.2)
        self.play(
            FadeIn(log),
            FadeIn(pi),
            FadeIn(logsqr),
            FadeIn(pisqr),
            FadeIn(olog),
        )
        self.wait(4)
        self.play(
            FadeOut(log),
            FadeOut(pi),
            FadeOut(logsqr),
            FadeOut(pisqr),
            FadeOut(olog),
            FadeOut(var),
            FadeOut(varmod),
            FadeOut(equals),
            FadeOut(expr_1),
            FadeOut(exprmod_1),
            FadeOut(sum),
            FadeOut(expr_2),
            FadeOut(exprmod_2)
        )
        im1 = ImageMobject("imagen2.png").scale(2.5).move_to(UP*3)
        im2 = ImageMobject("imagen5.png").scale(2.5).next_to(im1,DOWN*0.9)
        im3 = ImageMobject("imagen1.png").scale(2.5).next_to(im2,DOWN*0.9)
        im4 = ImageMobject("imagen3.png").scale(2.5).next_to(im3,DOWN*0.9)
        im5 = ImageMobject("imagen4.png").scale(2.5).next_to(im4,DOWN*0.9)
        self.play(
            FadeIn(im1),
            FadeIn(im2),
            FadeIn(im3),
            FadeIn(im4),
            FadeIn(im5),
        )
        self.wait(4)
        im6 = ImageMobject("imagen6.png").scale(1.5).move_to(RIGHT * 3)
        self.play(
            im1.animate.move_to(LEFT*4+UP*3),
            im2.animate.move_to(LEFT*4+UP*1.5),
            im3.animate.move_to(LEFT*4),
            im4.animate.move_to(LEFT*4+DOWN*1.5),
            im5.animate.move_to(LEFT*4+DOWN*3),
            FadeIn(im6)
        )
        self.wait(4)
        self.play(
            FadeOut(im1),
            FadeOut(im2),
            FadeOut(im3),
            FadeOut(im4),
            FadeOut(im5),
            FadeOut(im6)
        )
        gracias = Tex("Gracias").scale(5)
        self.play(Write(gracias))
        self.wait(4)