Vim�UnDo� ����=����J�]`��J}�o��C���ck�   -           return se   -         :       :   :   :    e��    _�                             ����                                                                                                                                                                                                                                                                                                                                                             e��     �                 # Create your models here.5��                                                �                                                �                                                5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             e�     �                 class Knight5��                         +                      5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             e�     �                 class Knight()5��                         ,                      �                         9                      �                         :                      �                          ;                      5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             e�     �                     KINGDOMS = 5��                         J                      5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             e�     �                           �             �                   KINGDOMS = (�                            )�                     KINGDOMS = ()5��                        K                      �                         L                     �                        K                      �                         L                     �                        T                     5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             e�     �                       �             �                       ('C', 'Camelot'),5��                        e               	       �                         n                      5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             e�     �                       ('G', 'Gondor'),5��                         ~                      �                        ~                     �                         ~                      5�_�      	                     ����                                                                                                                                                                                                                                                                                                                                                             e�     �                        ('G', 'Gondor'),5��                          f                      5�_�      
           	          ����                                                                                                                                                                                                                                                                                                                                                             e�     �                       ('C', 'Camelot'),5��       
                 V                     5�_�   	              
          ����                                                                                                                                                                                                                                                                                                                                                             e�     �             5��                          l               	       5�_�   
                        ����                                                                                                                                                                                                                                                                                                                                                             e�     �                       5��                         t                      5�_�                       	    ����                                                                                                                                                                                                                                                                                                                                                             e�      �               
        ()5��       	                  u                      5�_�                       
    ����                                                                                                                                                                                                                                                                                                                                                             e�      �                       ("")�             5��       
                  v                      �                        |                     5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             e�#     �      	                 ("wales"", "Wales"),5��                        �               	       5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             e�&     �      	   	              5��                         �                      5�_�                       	    ����                                                                                                                                                                                                                                                                                                                                                             e�&     �      	   	      
        ()5��       	                  �                      5�_�                       
    ����                                                                                                                                                                                                                                                                                                                                                             e�&     �      	   	              ("")�      	   	    5��       
                 �                     5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             e�(     �      
   	              ("orkney", "Orkney"),5��                        �               	       �                         �                      �       	                  �                      �                         �                      5�_�                    	       ����                                                                                                                                                                                                                                                                                                                                                             e�-     �      
   
              5��                         �                      5�_�                    	   	    ����                                                                                                                                                                                                                                                                                                                                                             e�-     �      
   
      
        ()5��       	                  �                      5�_�                    	   
    ����                                                                                                                                                                                                                                                                                                                                                             e�.     �      
   
              ("")5��       
                  �                      �                         �                      �       
                 �                     �                         �                      �                         �                      5�_�                    	       ����                                                                                                                                                                                                                                                                                                                                                             e�6     �      	                  ("va")5��                          �                      5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             e�:     �         	              ("wales"", "Wales"),5��                         |                      5�_�                    	       ����                                                                                                                                                                                                                                                                                                                                                             e�<     �   
                  name = m�               �   	                  �   	            5��    	                      �                      �    	                     �                     �    	                      �                      �    	                     �                      �    
                  '   �               '       5�_�                       +    ����                                                                                                                                                                                                                                                                                                                                                             e�?     �                     age = models.Posi�               �   
              +    name = models.CharField(max_length=100)5��    
   +                 �                      �                      #   �               #       5�_�                       '    ����                                                                                                                                                                                                                                                                                                                                                             e�G     �                 '    age = models.PositiveIntegerField()5��       '                                      �                                              �                                            5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             e�Z     �                     lady = models.ForeignKey5��                         %                     5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             e�Z     �                     lady = models.ForeignKey()5��                         &                     5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             e�[     �                     king�               �                      lady = models.ForeignKey("")5��                         '                     �       #                  ,                     �       1                  :                     �       /                  8                     �       J                S                    �                         T                    �       !                  u                     �       (                 |                     �                      @   }             @       5�_�                       @    ����                                                                                                                                                                                                                                                                                                                                                             e�t     �                     quests = mo�               �                 @    kingdom = models.CharField(max_length=100, choices=KINGDOMS)5��       @                 �                     �                      4   �              4       5�_�                        7    ����                                                                                                                                                                                                                                                                                                                                                             e�{     �                     objects = mo�               �                     �               5��                          �                     �                          �                     �                         �                     �                         �                     5�_�      !                      ����                                                                                                                                                                                                                                                                                                                                                             e�     �                     camelot = C�               �                     objects = models.Manager()5��                                             �                                              �                        "                    5�_�       "           !           ����                                                                                                                                                                                                                                                                                                                                                             e��     �               class�             �                �             5��                                                �                                                �                       %                  %       5�_�   !   #           "      %    ����                                                                                                                                                                                                                                                                                                                                                             e��     �                   def �             �               %class CamelotManager(models.Manager):5��       %                  D                      �                          E                      �                     ?   M               S       5�_�   "   $           #      ?    ����                                                                                                                                                                                                                                                                                                                                                             e��     �      	         ?        return super().get_queryset().filter(kingdom="camelot")5��       ?                 �               	       �                         �                     �                          �                      �                         �                      �                      
   �               
       5�_�   #   %           $          ����                                                                                                                                                                                                                                                                                                                                                             e��     �      	             def quests5��                         �                      5�_�   $   &           %          ����                                                                                                                                                                                                                                                                                                                                                             e��     �                       �   	   
       �      
             def quests()5��                      
   �               
       �                        �                     �                        �                     �       !                  �                      �       "                 �                      �                         �                     �                     	   �               p       5�_�   %   '           &   	       ����                                                                                                                                                                                                                                                                                                                                                             e��     �      	          H        return self.get_queryset().filter(name=knight_name).values_list(   %            "quests__name", flat=True5��                          �       o               5�_�   &   (           '   	       ����                                                                                                                                                                                                                                                                                                                                                             e��     �      	          	        )5��                          �       
               5�_�   '   )           (           ����                                                                                                                                                                                                                                                                                                                                                             e��     �      
                 �      
       5��                          �                      �                          �                      5�_�   (   *           )   	        ����                                                                                                                                                                                                                                                                                                                                                             e��     �      
                  return self.get_queryset5��                          �                      5�_�   )   +           *   	   "    ����                                                                                                                                                                                                                                                                                                                                                             e��     �      
         "        return self.get_queryset()5��       "                  �                      5�_�   *   ,           +   	   &    ����                                                                                                                                                                                                                                                                                                                                                             e��     �      
         &        return self.get_queryset().get5��       &                  �                      5�_�   +   -           ,   	   '    ����                                                                                                                                                                                                                                                                                                                                                             e��     �      
         (        return self.get_queryset().get()�   	   
       5��       '                 �                     5�_�   ,   .           -   
        ����                                                                                                                                                                                                                                                                                                                                                             e��     �   
             �   
          5��    
                                           �    
                                           �                       
                 
       5�_�   -   /           .      
    ����                                                                                                                                                                                                                                                                                                                                                             e��     �               
class Lady5��       
                                       5�_�   .   0           /          ����                                                                                                                                                                                                                                                                                                                                                             e��     �               class Lady()�             5��                                            5�_�   /   1           0          ����                                                                                                                                                                                                                                                                                                                                                             e��     �                   �             �               class Lady(models.Model):5��                         &                     �                          '                     �                     '   +              O       5�_�   0   2           1      '    ����                                                                                                                                                                                                                                                                                                                                                             e��     �               '    age = models.PositiveIntegerField()�             5��       '                 z              1       5�_�   1   3           2          ����                                                                                                                                                                                                                                                                                                                                                             e��     �         !              return self.name5��                        �              	       �                         �                    �                          �                     �                         �                     �                         �                    5�_�   2   4           3          ����                                                                                                                                                                                                                                                                                                                                                             e��     �         #      class Quest5��                         �                     5�_�   3   5           4          ����                                                                                                                                                                                                                                                                                                                                                             e��     �         #      class Quest()�         #    5��                        �                    5�_�   4   6           5          ����                                                                                                                                                                                                                                                                                                                                                             e��     �         $          �         $    �         #      class Quest(models.Model):5��                         �                     �                          �                     �                        �              }       5�_�   5   7           6          ����                                                                                                                                                                                                                                                                                                                                                             e��     �         (              return self.name5��                        I              	       �                         J                    �                          J                     �                         J                     �                          K                     5�_�   6   8           7           ����                                                                                                                                                                                                                                                                                                                                                             e��    �               *   from django.db import models           %class CamelotManager(models.Manager):       def get_queryset(self):   ?        return super().get_queryset().filter(kingdom="camelot")       "    def quests(self, knight_name):   E        return self.get_queryset().get(name=knight_name).quests.all()           class Lady(models.Model):   +    name = models.CharField(max_length=100)   '    age = models.PositiveIntegerField()           def __str__(self):           return self.name       class Quest(models.Model):   +    name = models.CharField(max_length=100)   $    description = models.TextField()           def __str__(self):           return self.name           class Knight(models.Model):       KINGDOMS = (           ('camelot', 'Camelot'),           ("wales", "Wales"),           ("orkney", "Orkney"),               )       +    name = models.CharField(max_length=100)   '    age = models.PositiveIntegerField()   J    lady = models.ForeignKey("Lady", on_delete=models.SET_NULL, null=True,   (                             blank=True)   @    kingdom = models.CharField(max_length=100, choices=KINGDOMS)   8    quests = models.ManyToManyField("Quest", blank=True)           objects = models.Manager()       camelot = CamelotManager()5��            *       *               c      ?      5�_�   7   9           8   *        ����                                                                                                                                                                                                                                                                                                                                                             e��     �   *                  �   *            5��    *                      ?                     �    *                      ?                     �    *                     ?                     �    +                     D                     5�_�   8   :           9   ,       ����                                                                                                                                                                                                                                                                                                                                                             e��     �   +                  def __str__5��    +                     O                     5�_�   9               :   ,       ����                                                                                                                                                                                                                                                                                                                                                             e��    �   ,                      return se�   -            �   +                  def __str__()5��    +                     P                     �    +                     U                     �    +                    V                     �    ,                     W                    5��