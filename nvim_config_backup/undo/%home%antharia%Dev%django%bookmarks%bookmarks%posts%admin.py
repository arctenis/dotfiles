Vim�UnDo� ���}Vӯk�S���y��������:<�e�   
   (    list_filter = ('user', 'created_at')                             e�nX    _�                             ����                                                                                                                                                                                                                                                                                                                                                             e�A�     �               @�             �                �             5��                          !                      �                          !                      �                         9                      �                          :                      �                          ;                      5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             e�A�     �               @admin.register(Post)5��                         P                      �                          Q                      5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             e�A�     �               class PostAdmin5��                         `                      5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             e�A�     �                   �             �               class PostAdmin()5��                         a                      �       !                  r                      �       "                  s                      �                          t                      �                     $   x               5      5�_�                    
       ����                                                                                                                                                                                                                                                                                                                                                             e�A�     �   	   
              raw_id_fields = ('author',)5��    	                      J                      5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             e�A�     �   
            $    ordering = ['status', 'publish']5��    
                     y                     5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             e�A�     �   
                ordering = []5��    
                     y                     5�_�      	                     ����                                                                                                                                                                                                                                                                                                                                                             e�A�     �   
                ordering = [""]5��    
                  
   z              
       5�_�      
           	   
       ����                                                                                                                                                                                                                                                                                                                                                             e�A�     �   	                date_hierarchy = 'publish'5��    	          	           _      	               5�_�   	              
   
       ����                                                                                                                                                                                                                                                                                                                                                             e�A�     �   	                date_hierarchy = 5��    	                     _                     5�_�   
                 
       ����                                                                                                                                                                                                                                                                                                                                                             e�A�     �   	                date_hierarchy = ""5��    	                  
   `              
       5�_�                    	        ����                                                                                                                                                                                                                                                                                                                                                             e�A�     �      	          .    prepopulated_fields = {'slug': ('title',)}5��                                /               5�_�                           ����                                                                                                                                                                                                                                                                                                                                                v       e�A�     �      	         %    search_fields = ('title', 'body')5��              	           
      	               5�_�                           ����                                                                                                                                                                                                                                                                                                                                                v       e�B      �      	             search_fields = ('body')5��                                              5�_�                           ����                                                                                                                                                                                                                                                                                                                                                v       e�B     �               <    list_filter = ('status', 'created', 'publish', 'author')5��                        �                     5�_�                       #    ����                                                                                                                                                                                                                                                                                                                                                v       e�B     �               :    list_filter = ('user', 'created', 'publish', 'author')5��       #                  �                      5�_�                       '    ����                                                                                                                                                                                                                                                                                                                                                v       e�B     �               =    list_filter = ('user', 'created_at', 'publish', 'author')5��       '                  �                      5�_�                           ����                                                                                                                                                                                                                                                                                                                                                v       e�B     �               C    list_display = ('title', 'slug', 'author', 'publish', 'status')5��                        �                     5�_�                           ����                                                                                                                                                                                                                                                                                                                                                v       e�B     �               B    list_display = ('user', 'slug', 'author', 'publish', 'status')5��                        �                     �                     
   �              
       5�_�                       (    ����                                                                                                                                                                                                                                                                                                                                                v       e�B$     �               H    list_display = ('user', 'created_at', 'author', 'publish', 'status')5��       (                  �                      5�_�                            ����                                                                                                                                                                                                                                                                                                                                                v       e�B'    �   
                 # Register your models here.5��    
                      %                     5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             e�nT     �         
      )    list_display = ('user', 'created_at')5��                        �                     5�_�                            ����                                                                                                                                                                                                                                                                                                                                                             e�nW    �         
      (    list_filter = ('user', 'created_at')5��                        �                     5��