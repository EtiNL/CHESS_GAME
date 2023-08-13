import pygame
from pygame.locals import *
import src.graphic_interface.cevent as cevent
import src.graphic_interface.gui_pieces as gui_pieces

class App(cevent.CEvent,gui_pieces.GUI_pieces):
    def __init__(self, pieces):
        self._running = True
        self._display_surf = None
        self._image_surf = None
        self.pieces = pieces

    def on_init(self):
        pygame.init()
        self._display_surf = pygame.display.set_mode((1000,1000), pygame.HWSURFACE)
        pygame.display.set_caption("Chess game")
        self._running = True

        'loading board image'
        self._image_surf = pygame.image.load("src/graphic_interface/Chessboard.jpeg").convert()
        self._display_surf.blit(self._image_surf,(0,0))

        'loading pieces'
        self.white_pieces=[]
        for piece in self.pieces['w']:
            self.white_pieces.append(gui_pieces.GUI_pieces(piece.piece_type, 'w', [piece.row,piece.file]))
        self.black_pieces=[]
        for piece in self.pieces['b']:
            self.black_pieces.append(gui_pieces.GUI_pieces(piece.piece_type, 'b', [piece.row,piece.file]))

    def on_loop(self):
        pass

    def on_render(self):
        self._display_surf.blit(self._image_surf,(0,0))
        for piece in self.white_pieces:
            self._display_surf.blit(piece.image,piece.image_pos)
        for piece in self.black_pieces:
            self._display_surf.blit(piece.image,piece.image_pos)
        pygame.display.update()

    def on_cleanup(self):
        pygame.quit()

    def on_exit(self):
        self._running = False

    def on_execute(self):
        if self.on_init() == False:
            self._running = False

        while( self._running ):
            for event in pygame.event.get():
                self.on_event(event)
            self.on_loop()
            self.on_render()
        self.on_cleanup()

if __name__ == "__main__" :
    theApp = App()
    theApp.on_execute()
