class show:
    def __init__(l,self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    brect.x=c_pos[0]
                    brect.y=c_pos[1]
                    self.blit(back,brect)
                    self.blit(front,frect)
                    self.blit(left,lrect)
                    self.blit(right,rrect)
                    self.blit(back_run,brrect)
                    self.blit(front_run,frrect)
                    self.blit(left_run,lrrect)
                    self.blit(right_run,rrrect)
                    self.blit(front_run_flip,frfrect)
                    self.blit(back_run_flip,brfrect)
