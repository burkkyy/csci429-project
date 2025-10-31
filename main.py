from scenes import *


class Main(Scene):
    def construct(self):
        scenes = [Introduction]
        for scene in scenes:
            # Play the scene
            scene.construct(self)

            # Fade out the scene for next scene
            animations = []
            for mobject in self.mobjects:
                animations.append(FadeOut(mobject))
            self.play(*animations)
