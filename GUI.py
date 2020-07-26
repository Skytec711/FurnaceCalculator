import pygame
import Colors
class GUI:
    def __init__(self, width, height, x, y, pixelsize, screen):
        self.pixelsize = pixelsize
        self.screen = screen
        self.offsetx = x - width / 2
        self.offsety = y - height / 2

        self.edgewhite_surface = pygame.Surface((width - self.pixelsize * 6, height - self.pixelsize * 6))
        self.edgewhite_surface.fill(Colors.white)
        self.edgewhite_rect = self.edgewhite_surface.get_rect(top=self.pixelsize * 2 + self.offsety, left=self.pixelsize * 2 + self.offsetx)

        self.edgegrey_surface = pygame.Surface((width - self.pixelsize * 6, height - self.pixelsize * 6))
        self.edgegrey_surface.fill(Colors.grey4)
        self.edgegrey_rect = self.edgegrey_surface.get_rect(top=self.pixelsize * 4 + self.offsety, left=self.pixelsize * 4 + self.offsetx)

        self.background_surface = pygame.Surface((width - self.pixelsize * 8, height - self.pixelsize * 8))
        self.background_surface.fill(Colors.grey)
        self.background_rect = self.background_surface.get_rect(top=self.pixelsize * 4 + self.offsety, left=self.pixelsize * 4 + self.offsetx)

        self.edgetopleft_surface = pygame.Surface((self.pixelsize, self.pixelsize))
        self.edgetopleft_surface.fill(Colors.white)
        self.edgetopleft_rect = self.edgetopleft_surface.get_rect(top=self.pixelsize * 4 + self.offsety, left=self.pixelsize * 4 + self.offsetx)

        self.edgetopright_surface = pygame.Surface((self.pixelsize, self.pixelsize))
        self.edgetopright_surface.fill(Colors.grey)
        self.edgetopright_rect = self.edgetopright_surface.get_rect(top=self.pixelsize * 3 + self.offsety, right=width - self.pixelsize * 3 + self.offsetx)

        self.edgebottomleft_surface = pygame.Surface((self.pixelsize, self.pixelsize))
        self.edgebottomleft_surface.fill(Colors.grey)
        self.edgebottomleft_rect = self.edgebottomleft_surface.get_rect(bottom=height - self.pixelsize * 3 + self.offsety, left=self.pixelsize * 3 + self.offsetx)

        self.edgebottomright_surface = pygame.Surface((self.pixelsize, self.pixelsize))
        self.edgebottomright_surface.fill(Colors.grey4)
        self.edgebottomright_rect = self.edgebottomright_surface.get_rect(bottom=height - self.pixelsize * 4 + self.offsety, right=width - self.pixelsize * 4 + self.offsetx)

        self.borderleft_surface = pygame.Surface((self.pixelsize, height - self.pixelsize * 7))
        self.borderleft_surface.fill(Colors.black)
        self.borderleft_rect = self.borderleft_surface.get_rect(top=self.pixelsize * 3 + self.offsety, left=self.pixelsize + self.offsetx)

        self.borderright_surface = pygame.Surface((self.pixelsize, height - self.pixelsize * 7))
        self.borderright_surface.fill(Colors.black)
        self.borderright_rect = self.borderright_surface.get_rect(top=self.pixelsize * 4 + self.offsety, right=width - self.pixelsize + self.offsetx)

        self.bordertop_surface = pygame.Surface((width - self.pixelsize * 7, self.pixelsize))
        self.bordertop_surface.fill(Colors.black)
        self.bordertop_rect = self.bordertop_surface.get_rect(top=self.pixelsize + self.offsety, left=self.pixelsize * 3 + self.offsetx)

        self.borderbottom_surface = pygame.Surface((width - self.pixelsize * 7, self.pixelsize))
        self.borderbottom_surface.fill(Colors.black)
        self.borderbottom_rect = self.borderbottom_surface.get_rect(bottom=height - self.pixelsize + self.offsety, left=self.pixelsize * 4 + self.offsetx)

        self.bordertopleft_surface = pygame.Surface((self.pixelsize, self.pixelsize))
        self.bordertopleft_surface.fill(Colors.black)
        self.bordertopleft_rect = self.bordertopleft_surface.get_rect(top=self.pixelsize * 2 + self.offsety, left=self.pixelsize * 2 + self.offsetx)

        self.bordertopright1_surface = pygame.Surface((self.pixelsize, self.pixelsize))
        self.bordertopright1_surface.fill(Colors.black)
        self.bordertopright1_rect = self.bordertopright1_surface.get_rect(top=self.pixelsize * 2 + self.offsety, right=width - self.pixelsize * 3 + self.offsetx)

        self.bordertopright2_surface = pygame.Surface((self.pixelsize, self.pixelsize))
        self.bordertopright2_surface.fill(Colors.black)
        self.bordertopright2_rect = self.bordertopright2_surface.get_rect(top=self.pixelsize * 3 + self.offsety, right=width - self.pixelsize * 2 + self.offsetx)

        self.borderbottomleft1_surface = pygame.Surface((self.pixelsize, self.pixelsize))
        self.borderbottomleft1_surface.fill(Colors.black)
        self.borderbottomleft1_rect = self.borderbottomleft1_surface.get_rect(bottom=height - self.pixelsize * 3 + self.offsety, left=self.pixelsize * 2 + self.offsetx)

        self.borderbottomleft2_surface = pygame.Surface((self.pixelsize, self.pixelsize))
        self.borderbottomleft2_surface.fill(Colors.black)
        self.borderbottomleft2_rect = self.borderbottomleft2_surface.get_rect(bottom=height - self.pixelsize * 2 + self.offsety, left=self.pixelsize * 3 + self.offsetx)

        self.borderbottomright_surface = pygame.Surface((self.pixelsize, self.pixelsize))
        self.borderbottomright_surface.fill(Colors.black)
        self.borderbottomright_rect = self.borderbottomright_surface.get_rect(bottom=height - self.pixelsize * 2 + self.offsety, right=width - self.pixelsize * 2 + self.offsetx)

    def resize(self, width, height, x, y):
        self.offsetx = x - width / 2
        self.offsety = y - height / 2

        self.edgewhite_surface = pygame.Surface((width - self.pixelsize * 6, height - self.pixelsize * 6))
        self.edgewhite_surface.fill(Colors.white)
        self.edgewhite_rect = self.edgewhite_surface.get_rect(top=self.pixelsize * 2 + self.offsety, left=self.pixelsize * 2 + self.offsetx)

        self.edgegrey_surface = pygame.Surface((width - self.pixelsize * 6, height - self.pixelsize * 6))
        self.edgegrey_surface.fill(Colors.grey4)
        self.edgegrey_rect = self.edgegrey_surface.get_rect(top=self.pixelsize * 4 + self.offsety, left=self.pixelsize * 4 + self.offsetx)

        self.background_surface = pygame.Surface((width - self.pixelsize * 8, height - self.pixelsize * 8))
        self.background_surface.fill(Colors.grey)
        self.background_rect = self.background_surface.get_rect(top=self.pixelsize * 4 + self.offsety, left=self.pixelsize * 4 + self.offsetx)

        self.edgetopleft_rect = self.edgetopleft_surface.get_rect(top=self.pixelsize * 4 + self.offsety, left=self.pixelsize * 4 + self.offsetx)

        self.edgetopright_rect = self.edgetopright_surface.get_rect(top=self.pixelsize * 3 + self.offsety, right=width - self.pixelsize * 3 + self.offsetx)

        self.edgebottomleft_rect = self.edgebottomleft_surface.get_rect(bottom=height - self.pixelsize * 3 + self.offsety, left=self.pixelsize * 3 + self.offsetx)

        self.edgebottomright_rect = self.edgebottomright_surface.get_rect(bottom=height - self.pixelsize * 4 + self.offsety, right=width - self.pixelsize * 4 + self.offsetx)

        self.borderleft_surface = pygame.Surface((self.pixelsize, height - self.pixelsize * 7))
        self.borderleft_surface.fill(Colors.black)
        self.borderleft_rect = self.borderleft_surface.get_rect(top=self.pixelsize * 3 + self.offsety, left=self.pixelsize + self.offsetx)

        self.borderright_surface = pygame.Surface((self.pixelsize, height - self.pixelsize * 7))
        self.borderright_surface.fill(Colors.black)
        self.borderright_rect = self.borderright_surface.get_rect(top=self.pixelsize * 4 + self.offsety, right=width - self.pixelsize + self.offsetx)

        self.bordertop_surface = pygame.Surface((width - self.pixelsize * 7, self.pixelsize))
        self.bordertop_surface.fill(Colors.black)
        self.bordertop_rect = self.bordertop_surface.get_rect(top=self.pixelsize + self.offsety, left=self.pixelsize * 3 + self.offsetx)

        self.borderbottom_surface = pygame.Surface((width - self.pixelsize * 7, self.pixelsize))
        self.borderbottom_surface.fill(Colors.black)
        self.borderbottom_rect = self.borderbottom_surface.get_rect(bottom=height - self.pixelsize + self.offsety, left=self.pixelsize * 4 + self.offsetx)

        self.bordertopleft_rect = self.bordertopleft_surface.get_rect(top=self.pixelsize * 2 + self.offsety, left=self.pixelsize * 2 + self.offsetx)

        self.bordertopright1_rect = self.bordertopright1_surface.get_rect(top=self.pixelsize * 2 + self.offsety, right=width - self.pixelsize * 3 + self.offsetx)

        self.bordertopright2_rect = self.bordertopright2_surface.get_rect(top=self.pixelsize * 3 + self.offsety, right=width - self.pixelsize * 2 + self.offsetx)

        self.borderbottomleft1_rect = self.borderbottomleft1_surface.get_rect(bottom=height - self.pixelsize * 3 + self.offsety, left=self.pixelsize * 2 + self.offsetx)

        self.borderbottomleft2_rect = self.borderbottomleft2_surface.get_rect(bottom=height - self.pixelsize * 2 + self.offsety, left=self.pixelsize * 3 + self.offsetx)

        self.borderbottomright_rect = self.borderbottomright_surface.get_rect(bottom=height - self.pixelsize * 2 + self.offsety, right=width - self.pixelsize * 2 + self.offsetx)

    def draw(self):
        self.screen.blit(self.edgewhite_surface, self.edgewhite_rect)

        self.screen.blit(self.edgegrey_surface, self.edgegrey_rect)

        self.screen.blit(self.background_surface, self.background_rect)
        
        self.screen.blit(self.edgetopleft_surface, self.edgetopleft_rect)

        self.screen.blit(self.edgetopright_surface, self.edgetopright_rect)

        self.screen.blit(self.edgebottomleft_surface, self.edgebottomleft_rect)

        self.screen.blit(self.edgebottomright_surface, self.edgebottomright_rect)

        self.screen.blit(self.borderleft_surface, self.borderleft_rect)
        
        self.screen.blit(self.borderright_surface, self.borderright_rect)

        self.screen.blit(self.bordertop_surface, self.bordertop_rect)

        self.screen.blit(self.borderbottom_surface, self.borderbottom_rect)

        self.screen.blit(self.bordertopleft_surface, self.bordertopleft_rect)

        self.screen.blit(self.bordertopright1_surface, self.bordertopright1_rect)

        self.screen.blit(self.bordertopright2_surface, self.bordertopright2_rect)

        self.screen.blit(self.borderbottomleft1_surface, self.borderbottomleft1_rect)

        self.screen.blit(self.borderbottomleft2_surface, self.borderbottomleft2_rect)

        self.screen.blit(self.borderbottomright_surface, self.borderbottomright_rect)