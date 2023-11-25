from manim import *


class Identidades(Scene):
    def construct(self):

        text_transition = Text("Entonces nos interesan las constantes de tipo:", font_size = 30, color = YELLOW)
        bbc_formula = MathTex("\\sum_{k = 0}^{\\infty}\\frac{p(k)}{b^{ck}q(k)}").scale(1.5)
        VGroup(
            text_transition,
            bbc_formula,
        ).arrange(DOWN)
        self.play(Write(text_transition),FadeIn(bbc_formula))
        self.wait(2.5)
        self.play(
            FadeOut(text_transition),
            FadeOut(bbc_formula),
        )
        self.wait(1)

        # Title
        title = Text("Las Identidades", font_size=50, color = WHITE)
        self.play(Write(title))
        self.wait(1)

        # Clear the screen
        self.play(FadeOut(title))
        self.wait(1)

        # Set style for formulas
        formula_style = {"tex_to_color_map": {
            "{\\pi}": YELLOW, "{\\log(2)}": BLUE, "{\\log(9/10)}": GREEN, "{\\pi^2}": RED,
            "{\\frac{1}{16^i}\\left(\\frac{4}{8i+1}-\\frac{2}{8i+4}-\\frac{1}{8i+5}-\\frac{1}{8i+6}\\right)}": BLUE,
            "{\\frac{1}{k 2^k}}": RED,
            "{\\frac{-1}{10^{k-1}k}}": ORANGE,
            "{\\frac{a_i}{2^i i^2}}": GREEN,
            "{\\frac{b_i}{2^i i^2}}": YELLOW,
            "a_i = [1,-3,-2,-3,1,0]": RED,
            "b_i = [2,-10,-7,-10,2,-1]": BLUE,
            "{\\frac{1}{10^{k-1}k}}": YELLOW,
            "{\\log^2(2)}": BLUE
        }}

        # Decorations
        
        # Identities
        identities = [
            "{\\pi} = \\sum_{i=1}^\\infty {\\frac{1}{16^i}\\left(\\frac{4}{8i+1}-\\frac{2}{8i+4}-\\frac{1}{8i+5}-\\frac{1}{8i+6}\\right)}",
            "{\\log(2)} = \\sum_{k=0}^\\infty {\\frac{1}{k 2^k}}",
            "{\\log(9/10)} = \\frac{-1}{10}\\sum_{k=1}^\\infty {\\frac{1}{10^{k-1}k}}",
            "{\\pi^2} = 36 \\sum_{i=1}^\\infty {\\frac{a_i}{2^i i^2}}",
            "a_i = [1,-3,-2,-3,1,0]",
            "{\\log^2(2)} = 2 \\sum_{i=1}^\\infty {\\frac{b_i}{2^i i^2}}",
            "b_i = [2,-10,-7,-10,2,-1]"
        ]

        text1 = MathTex(identities[0], **formula_style, font_size=30).scale(1.5)
        self.play(Write(text1))
        self.wait(2)
        self.play(FadeOut(text1))
        self.wait(0.7)

        text2 = MathTex(identities[1], **formula_style, font_size=30).scale(1.5)
        self.play(Write(text2))
        self.wait(2)
        self.play(FadeOut(text2))
        self.wait(0.7)

        text3 = MathTex(identities[2], **formula_style, font_size=30).scale(1.5)
        self.play(Write(text3))
        self.wait(2)
        self.play(FadeOut(text3))
        self.wait(0.7)

        text4 = MathTex(identities[3], **formula_style, font_size=30).scale(1.5)
        text5 = MathTex(identities[4], **formula_style, font_size=30).scale(1.5)
        
        VGroup(text4, text5).arrange(DOWN)
        self.play(
            Write(text4),
            Write(text5),
        )
        self.wait(0.7)
        self.play(
            FadeOut(text4),
            FadeOut(text5),
        )


        text6 = MathTex(identities[5], **formula_style, font_size=30).scale(1.5)
        text7 = MathTex(identities[6], **formula_style, font_size=30).scale(1.5)
        
        VGroup(text6, text7).arrange(DOWN)
        self.play(
            Write(text6),
            Write(text7),
        )
        self.wait(1.5)



class TeoremaPi(Scene):
    def construct(self):
        # Set style for equations
        equation_style = {"tex_to_color_map": {
            "\\frac{x^{k-1}}{1-x^8}": YELLOW,
            "\\sum_{i=0}^\\infty x^{8i+k-1}": GREEN,
            "\\frac{1}{2^{k/2}}\\sum_{i=0}^\\infty \\frac{1}{16^i(8i+k)}": RED,
            "\\sum_{i=0}^\\infty \\frac{-\\frac{2}{8i+4}-\\frac{1}{8i+5}-\\frac{1}{8i+6}+\\frac{4}{8i+1}}{16^i}": BLUE,
            "\\int_0^{\\frac{1}{\\sqrt{2}}} \\frac{-8x^5-4\\sqrt{2}x^4-8x^3+4\\sqrt{2}}{1-x^8} \\, dx": YELLOW,
            "\\pi": ORANGE,
            "\\sum_{i=0}^\\infty \\frac{1}{16^i}\\left(-\\frac{2}{8i+4}-\\frac{1}{8i+5}-\\frac{1}{8i+6}+\\frac{4}{8i+1}\\right)": BLUE
        }}

        # Additional text
        text0 = Text("Se puede verificar en Mathematica que", font_size=30, color=WHITE)
        self.play(Write(text0))
        self.wait(0.5)
        self.play(FadeOut(text0))

        equation0 = MathTex("\\pi", "=", "\\int_0^{\\frac{1}{\\sqrt{2}}} \\frac{-8x^5-4\\sqrt{2}x^4-8x^3+4\\sqrt{2}}{1-x^8} \\, dx").scale(1.5)
        equation0.set_color_by_tex_to_color_map(equation_style["tex_to_color_map"])
        
        self.play(Write(equation0))
        self.wait(2)
        self.play(FadeOut(equation0))

        text01 = Text("Por otro lado,")
        self.play(Write(text01))
        self.wait(1)
        self.play(FadeOut(text01))

        # Equation 1
        equation1 = MathTex("\\int_0^{\\frac{1}{\\sqrt{2}}} \\frac{x^{k-1}}{1-x^8} \\, dx", "=", "\\int_0^{\\frac{1}{\\sqrt{2}}} \\sum_{i=0}^\\infty x^{8i+k-1} \\, dx").scale(1.5)
        equation1.set_color_by_tex_to_color_map(equation_style["tex_to_color_map"])
        
        # Equation 2
        equation2 = MathTex("\\int_0^{\\frac{1}{\\sqrt{2}}} \\frac{x^{k-1}}{1-x^8} \\, dx","=","\\int_0^{\\frac{1}{\\sqrt{2}}} \\sum_{i=0}^\\infty x^{8i+k-1} \\, dx", "=", "\\frac{1}{2^{k/2}}\\sum_{i=0}^\\infty \\frac{1}{16^i(8i+k)}").scale(0.9)
        equation2.set_color_by_tex_to_color_map(equation_style["tex_to_color_map"])

        equation21 = MathTex("\\int_0^{\\frac{1}{\\sqrt{2}}} \\frac{x^{k-1}}{1-x^8} \\, dx","=", "\\frac{1}{2^{k/2}}\\sum_{i=0}^\\infty \\frac{1}{16^i(8i+k)}").scale(1.5)
        equation21.set_color_by_tex_to_color_map(equation_style["tex_to_color_map"])
        
        equation4 = MathTex("\\sum_{i=0}^\\infty \\frac{1}{16^i}\\left(-\\frac{2}{8i+4}-\\frac{1}{8i+5}-\\frac{1}{8i+6}+\\frac{4}{8i+1}\\right)",
                           "=", "\\int_0^{\\frac{1}{\\sqrt{2}}} \\frac{-8x^5-4\\sqrt{2}x^4-8x^3+4\\sqrt{2}}{1-x^8} \\, dx","=","\\pi").scale(0.7)
        equation4.set_color_by_tex_to_color_map(equation_style["tex_to_color_map"])
        
        # Display equations and transition
        self.play(Write(equation1))
        self.wait(2)
        self.play(Transform(equation1, equation2))
        self.wait(2)
        self.play(Transform(equation1, equation21))
        self.wait(2)        
        self.play(FadeOut(equation1))
        
        # Additional text
        text = Text("Por lo tanto, podemos escribir:", font_size=30, color=WHITE)
        self.play(Write(text))
        self.wait(0.5)
        self.play(FadeOut(text))

        integral1 = MathTex("\\int_0^{\\frac{1}{\\sqrt{2}}} \\frac{-8x^5}{1-x^8} \\, dx","=","\\sum_{i=0}^\\infty \\frac{1}{16^i}\\left(\\frac{-1}{8i+6}\\right)").scale(1.5)
        
        lines1 = VGroup(*integral1.split())
        lines1.arrange(DOWN)
        self.play(Write(lines1))
        self.wait(1)

        # Frame 2
        integral2 = MathTex("\\int_0^{\\frac{1}{\\sqrt{2}}} \\frac{-8x^5}{1-x^8} \\, dx + \\int_0^{\\frac{1}{\\sqrt{2}}} \\frac{4\\sqrt(2)(1-x^4)}{1-x^8} \\, dx",
                            "=",
                            "\\sum_{i=0}^\\infty \\frac{1}{16^i}\\left(\\frac{-1}{8i+6}\\right)-\\sum_{i=0}^\\infty \\frac{1}{16^i}\\left(\\frac{-1}{8i+5}+\\frac{4}{8i+1}\\right)").scale(0.9)
        lines2 = VGroup(*integral2.split())
        lines2.arrange(DOWN)
        self.play(Transform(lines1, lines2))
        self.wait(1)

        # Frame 3
        integral3 = MathTex("\\int_0^{\\frac{1}{\\sqrt{2}}} \\frac{-8x^5}{1-x^8} \\, dx + \\int_0^{\\frac{1}{\\sqrt{2}}} \\frac{4\\sqrt(2)(1-x^4)}{1-x^8} \\, dx - \\int_0^{\\frac{1}{\\sqrt{2}}} \\frac{8x^3}{1-x^8} \\, dx",
                            "=",
                            "\\sum_{i=0}^\\infty \\frac{1}{16^i}\\left(\\frac{-1}{8i+6}\\right)-\\sum_{i=0}^\\infty \\frac{1}{16^i}\\left(\\frac{-1}{8i+5}+\\frac{4}{8i+1}\\right) - \\sum_{i=0}^\\infty \\frac{1}{16^i}\\left(\\frac{2}{8i+4}\\right)").scale(0.7)
        lines3 = VGroup(*integral3.split())
        lines3.arrange(DOWN)
        self.play(Transform(lines1, lines3))
        self.wait(1)
        self.play(FadeOut(lines1))

        # Display the next equation
        textofinal = Text("Así, reescribiendo tenemos")
        VGroup(textofinal, equation4).arrange(DOWN)
        self.play(
            Write(textofinal),
            FadeIn(equation4, shift=DOWN),
        )

        equation5 = MathTex("\\sum_{i=0}^\\infty \\frac{1}{16^i}\\left(-\\frac{2}{8i+4}-\\frac{1}{8i+5}-\\frac{1}{8i+6}+\\frac{4}{8i+1}\\right)",
                           "=","\\pi")
        equation5.set_color_by_tex_to_color_map(equation_style["tex_to_color_map"])
        self.play(FadeOut(textofinal), Transform(equation4,equation5))
        self.wait(3)


class Logarithms(Scene):
    def construct(self):
        # Formula 1
        formula1 = MathTex("\\log \\left(\\frac{1}{1-x}\\right) = \\sum _{n=1}^\\infty \\frac{x^n}{n}",
                           tex_to_color_map={"\\log": BLUE, "\\frac{1}{1-x}": GREEN, "\\sum _{n=1}^\\infty": RED, "\\frac{x^n}{n}": ORANGE})
        formula1.scale(1.5)

        # Text explaining the transformation
        text1 = Text("Recordemos de Series de Taylor:")
        text1.next_to(formula1, UP)

        self.play(Write(text1))
        self.play(Write(formula1))
        self.wait(3)

        # Formula 2
        formula2 = MathTex("\\log(2) = \\sum _{k=1}^\\infty \\frac{1}{k 2^k}",
                           tex_to_color_map={"\\log(2)": BLUE, "\\sum _{k=1}^\\infty": RED, "\\frac{1}{k 2^k}": ORANGE})
        formula2.scale(1.5)

        # Text explaining the transformation
        text2 = Text("Reemplazando por 1/2 obtenemos")
        text2.next_to(formula2, UP)

        self.play(Transform(text1, text2), Transform(formula1, formula2))
        self.wait(2)

        # Additional explanation
        text3 = Text("y reemplazando por 1/10 obtenemos")
        text3.next_to(formula1, DOWN)

        self.play(FadeOut(text1), Write(text3))
        self.wait(2)

        formula3 = MathTex("\\log(9/10) = -\\sum _{k=1}^\\infty \\frac{1}{k 10^k}",
                           tex_to_color_map={"\\log(9/10)": BLUE, "\\sum _{k=1}^\\infty": RED, "\\frac{1}{k 10^k}": ORANGE})
        formula3.scale(1.5)

        # Clean up
        self.play(FadeOut(text3), Transform(formula1, formula3))
        self.wait(2.5)


class DegreeTwo(Scene):
    def construct(self):
        # Text
        text_intro = Text("Ahora vamos a las identidades de grado 2:", font_size=30, color=WHITE)
        self.play(Write(text_intro))
        self.wait(1)

        # Equation 1
        equation1 = MathTex(
            "\\pi ^2 = 36 \\sum _{i=1}^\\infty \\frac{a_i}{2^i i^2}",
            "\\quad [a_i] = [1, -3, -2, -3, 1, 0]"
        ).scale(1.2)

        equation1.set_color_by_tex_to_color_map({
            "\\pi ^2": BLUE,
            "\\sum _{i=1}^\\infty": RED,
            "\\frac{a_i}{2^i i^2}": GREEN,
            "\\quad [a_i]": YELLOW,
            "[1, -3, -2, -3, 1, 0]": ORANGE
        })

        # Equation 2
        equation2 = MathTex(
            "\\text{Log}^2(2) = 2 \\sum _{i=1}^\\infty \\frac{b_i}{2^i i^2}",
            "\\quad [b_i] = [2, -10, -7, -10, 2, -1]"
        ).scale(1.2)

        equation2.set_color_by_tex_to_color_map({
            "\\text{Log}^2(2)": BLUE,
            "\\sum _{i=1}^\\infty": RED,
            "\\frac{b_i}{2^i i^2}": GREEN,
            "[b_i]": YELLOW,
            "[2, -10, -7, -10, 2, -1]": ORANGE
        })

        # Display equations with smooth transitions
        self.play(ReplacementTransform(text_intro, equation1[0]), run_time=2)
        self.wait(1)
        self.play(FadeIn(equation1[1]), run_time=1)
        self.wait(2)

        self.play(ReplacementTransform(equation1[0], equation2[0]), run_time=2)
        self.wait(1)
        self.play(ReplacementTransform(equation1[1], equation2[1]), run_time=2)
        self.wait(2)

class PruebaLog2(Scene):
    def construct(self):    
        # Text
        text1 = Text("Para esto, definimos la función Dilogarítmica como", font_size=30, color=YELLOW)
        text2 = MathTex("Li_2(z) = \\int_0^z \\frac{\\log[1 - z]}{z} \\, dz",
                        tex_to_color_map={"Li_2(z)": BLUE,"\\int_0^z \\frac{\\log[1 - z]}{z} \\, dz": GREEN}).next_to(text1, DOWN)
        # Display text and equation
        self.play(Write(text1))
        self.wait(1)
        self.play(Write(text2))
        self.wait(3.5)

        # Transformation 1
        text3 = Text("Al derivar, obtenemos que", font_size=30, color=YELLOW)
        equation1 = MathTex("\\frac{d}{dx} Li_2\\left(-\\frac{1}{x}\\right) = \\frac{\\log(1+x) - \\log(x)}{x}", 
                            tex_to_color_map={"\\frac{d}{dx} Li_2\\left(-\\frac{1}{x}\\right)": BLUE,"\\frac{\\log(1+x) - \\log(x)}{x}": GREEN}).next_to(text3, DOWN)
        self.play(ReplacementTransform(text1, text3), ReplacementTransform(text2,equation1))
        self.wait(3.5)

        # Transformation 2
        text4 = Text("y al integrar tenemos", font_size=30, color=YELLOW)
        equation2 = MathTex("Li_2\\left(-\\frac{1}{x}\\right) + Li_2(-x) = 2 Li_2(-1) - \\frac{1}{2}\\log^2(x)",
                            tex_to_color_map={"Li_2\\left(-\\frac{1}{x}\\right) + Li_2(-x)": BLUE,"2 Li_2(-1) - \\frac{1}{2}\\log^2(x)": GREEN}).next_to(text4, DOWN)
        self.play(ReplacementTransform(text3, text4), ReplacementTransform(equation1, equation2))
        self.wait(3.5)

        # Transformation 3
        text5 = Text("al tomar x = -1, obtenemos", font_size=30, color=YELLOW)
        equation3 = MathTex("2Li_2(1) = 2Li_2(-1) + \\frac{\\pi^2}{2} ",
                            tex_to_color_map={"2Li_2(1)": BLUE,"2Li_2(-1) + \\frac{\\pi^2}{2}": GREEN}).next_to(text5, DOWN)
        self.play(ReplacementTransform(text4, text5), ReplacementTransform(equation2, equation3))
        self.wait(3.5)

        # Transformation 4
        text6 = Text("Lo cual se puede reescribir como", font_size=25, color=YELLOW)
        equation4 = MathTex("\\pi^2 = 36 Li_2\\left(\\frac{1}{2}\\right) - 36 Li_2\\left(\\frac{1}{4}\\right) - 12 Li_2\\left(\\frac{1}{8}\\right) + 6 Li_2\\left(\\frac{1}{64}\\right)",
                            tex_to_color_map={"\\pi^2": BLUE,"36 Li_2\\left(\\frac{1}{2}\\right) - 36 Li_2\\left(\\frac{1}{4}\\right) - 12 Li_2\\left(\\frac{1}{8}\\right) + 6 Li_2\\left(\\frac{1}{64}\\right)": GREEN}).next_to(text6, DOWN)
        self.play(ReplacementTransform(text5, text6), ReplacementTransform(equation3, equation4))
        self.wait(2)

        # Transformation 5
        self.play(FadeOut(text6), FadeOut(equation4))
        text7 = Text("Por otro lado, tenemos", font_size=30, color=YELLOW)
        equation5 = MathTex("\\int_0^z \\frac{Log(1 - z)}{z} \\, dz = -\\log(z) \\log(1 - z) - \\int_0^z \\frac{\\log(z)}{1-z} \\, dz = -\\log(z) \\log(1 - z) - Li_2(1 - z) + Li_2(1)",
                            tex_to_color_map={"\\int_0^z \\frac{Log(1 - z)}{z} \\, dz": BLUE,"-\\log(z) \\log(1 - z) - \\int_0^z \\frac{\\log(z)}{1-z} \\, dz = -\\log(z) \\log(1 - z) - Li_2(1 - z) + Li_2(1)": GREEN}).scale(0.6).next_to(text7, DOWN)
        self.play(Write(text7), Write(equation5))
        self.wait(3.5)

        # Transformation 6
        text8 = Text("por lo tanto", font_size=30, color=YELLOW)
        equation6 = MathTex("Li_2(1 - z) + Li_2(z) = \\frac{\\pi^2}{6} - Log(z) Log(1 - z)",
                            tex_to_color_map={"Li_2(1 - z) + Li_2(z)": BLUE,"\\frac{\\pi^2}{6} - Log(z) Log(1 - z)": GREEN}).next_to(text8, DOWN)
        self.play(ReplacementTransform(text7, text8), ReplacementTransform(equation5, equation6))
        self.wait(3.5)

        # Transformation 7
        text9 = Text("y si z = 1/2, obtenemos la identidad", font_size=30, color=YELLOW)
        equation7 = MathTex("Li_2\\left(\\frac{1}{2}\\right) = \\frac{\\pi^2}{12} - \\frac{1}{2}\\log^2(2)",
                            tex_to_color_map={"Li_2\\left(\\frac{1}{2}\\right)": BLUE,"\\frac{\\pi^2}{12} - \\frac{1}{2}\\log^2(2)": GREEN}).next_to(text9, DOWN)
        self.play(ReplacementTransform(text8, text9), ReplacementTransform(equation6, equation7))
        self.wait(3.5)

        # Transformation 8
        text10 = Text("Y así, podemos obtener la identidad", font_size=30, color=WHITE)
        equation8 = MathTex("\\log^2(2) = 4 Li_2\\left(\\frac{1}{2}\\right) - 6 Li_2\\left(\\frac{1}{4}\\right) - 2 Li_2\\left(\\frac{1}{8}\\right) + Li_2\\left(\\frac{1}{64}\\right)",
                            tex_to_color_map={"\\log^2(2)": BLUE,"4 Li_2\\left(\\frac{1}{2}\\right) - 6 Li_2\\left(\\frac{1}{4}\\right) - 2 Li_2\\left(\\frac{1}{8}\\right) + Li_2\\left(\\frac{1}{64}\\right)": GREEN}).next_to(text10, DOWN)
        self.play(ReplacementTransform(text9, text10), ReplacementTransform(equation7, equation8))
        self.wait(3.5)


# See many more examples at https://docs.manim.community/en/stable/examples.html