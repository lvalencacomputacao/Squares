import pygame

class Musica:

    @staticmethod
    def ChangeVolume(command):
        volumeNow = pygame.mixer_music.get_volume()
        if command == pygame.K_DOWN:
            volume = max(0, volumeNow - 0.1)
        else:
            volume = min(1, volumeNow + 0.1)
        pygame.mixer_music.set_volume(volume)

    @staticmethod
    def mute(status):
        if status:
            pygame.mixer_music.stop()
        else:
            pygame.mixer_music.play(-1)