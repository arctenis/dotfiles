Vim�UnDo� P�8م~�g���V;�և��>�P��0:%
      3        group_name = request.POST.get('group_name')            ,       ,   ,   ,    eR�a    _�                             ����                                                                                                                                                                                                                                                                                                                                                             eQ4K     �                 # Create your views here.�               5��                      /   %              /       5�_�                       /    ����                                                                                                                                                                                                                                                                                                                                                             eQ4P     �                 /from .models import Member, Group, GiftExchange5��       /                  T                      �                          U                      �                          V                      �                         W                      �                         V                     �                        a                     5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             eQ4g     �                 def create_group5��                         f                      5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             eQ4h    �                     �               �                 def create_group()5��                         g                      �                         o                      �                         p                      �                       /   q               /       5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             eR@�     �                   �             5��                          q                      �                          q                      �                        x                      �                          y                      �                         x                      �                         x                      �                                               �                                              �                          �                      5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             eR@�     �                    if request5��                          q                      5�_�                            ����                                                                                                                                                                                                                                                                                                                                                             eR@�     �                   �             �             5��                          q                      �                           q                       5�_�      	                     ����                                                                                                                                                                                                                                                                                                                                                             eR@�     �                    if request.method == 'POST':5��                        �                     5�_�      
           	          ����                                                                                                                                                                                                                                                                                                                                                             eR@�     �         	              �         	    �             5��                          �                      �                      3   �              3       5�_�   	              
      3    ����                                                                                                                                                                                                                                                                                                                                                             eR@�     �      	   
          �      	   
    �      	   	      3        return render(request, 'create_group.html')5��       3                  �                      �       3                  �                      �       3                 �               	       �                      "   �              "       5�_�   
                    "    ����                                                                                                                                                                                                                                                                                                                                                             eR@�     �                       �   	   
       �      
   
      "    elif request.method == 'POST':5��       "                 �                      �                         �                     �                        �                     5�_�                    	        ����                                                                                                                                                                                                                                                                                                                            	                    V       eRA�    �      	                  # Create group   6        group = Group(name=request.POST['group_name'])           group.save()               # Create members           members = []   @        for i in range(1, int(request.POST['num_members']) + 1):   G            member = Member(name=request.POST['member_name_' + str(i)])               member.save()   "            members.append(member)               # Create gift exchange   1        gift_exchange = GiftExchange(group=group)           gift_exchange.save()   *        gift_exchange.members.set(members)           gift_exchange.save()5��                          �                     5�_�                           ����                                                                                                                                                                                                                                                                                                                            	          	          V       eRA�     �                       �   	   
       �      
   
    5��                          �                      �                         �                     �                        �                     5�_�                       .    ����                                                                                                                                                                                                                                                                                                                                                V       eRA�     �                 /    return render(request, 'create_group.html')5��       .                  &                     5�_�                       3    ����                                                                                                                                                                                                                                                                                                                                                V       eRA�     �                 5    return render(request, 'create_group.html', cont)5��       3                  +                     5�_�                            ����                                                                                                                                                                                                                                                                                                                                                V       eRA�     �                �             5��                          �                     �                          �                     �                         �                     �                         �                     �                         �                     �                        �                    �                                            5�_�                           ����                                                                                                                                                                                                                                                                                                                                                V       eRA�     �                   context = 5��                                              5�_�                           ����                                                                                                                                                                                                                                                                                                                                                V       eRA�     �                           �             �                   context = {�                            }�                   context = {}5��                                             �                                             �                                             �                                             �                                            5�_�                           ����                                                                                                                                                                                                                                                                                                                                                V       eRA�     �                       �             �                       'group': group,5��                                      	       �                         (                     5�_�                           ����                                                                                                                                                                                                                                                                                                                                                V       eRA�     �                       �             �                       'members': members,5��                        ;              	       �                         D                     5�_�                       '    ����                                                                                                                                                                                                                                                                                                                                                V       eRA�     �               '        'gift_exchange': gift_exchange,5��       '                 c              	       �                          d                     5�_�                            ����                                                                                                                                                                                                                                                                                                                                                V       eRA�     �                 5��                          d                     5�_�                           ����                                                                                                                                                                                                                                                                                                                                                V       eRA�     �                    context = {           'group': group,           'members': members,   '        'gift_exchange': gift_exchange,               }5��                          �      z               5�_�                           ����                                                                                                                                                                                                                                                                                                                                                 V       eRB�     �                    if request.method == 'GET':   3        return render(request, 'create_group.html')   "    elif request.method == 'POST':           # Create group   6        group = Group(name=request.POST['group_name'])           group.save()               # Create members           members = []   @        for i in range(1, int(request.POST['num_members']) + 1):   G            member = Member(name=request.POST['member_name_' + str(i)])               member.save()   "            members.append(member)               # Create gift exchange   1        gift_exchange = GiftExchange(group=group)           gift_exchange.save()   *        gift_exchange.members.set(members)           gift_exchange.save()    5��                          q       �              5�_�                           ����                                                                                                                                                                                                                                                                                                                                                 V       eRB�    �                   �             �             5��                          q                      �                          q                      5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             eRC�    �                 8    return render(request, 'create_group.html', context)5��                         �                      5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             eRC�     �                   �             �             5��                          �                      �                         �                      5�_�                            ����                                                                                                                                                                                                                                                                                                                                                             eRC�     �      	              if request.method == 'POST':5��                         �                      �                         �                     �                          �                      5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             eRC�    �                     if request.method == 'POST':5��                          �       !               5�_�                            ����                                                                                                                                                                                                                                                                                                                                                             eR��     �         	          �             5��                          q                      �                          q                      �                        u                     5�_�                            ����                                                                                                                                                                                                                                                                                                                                                             eR��     �         	          if request.method == 5��                         �                      5�_�      !                      ����                                                                                                                                                                                                                                                                                                                                                             eR��    �         
              �         
    �         	          if request.method == ""5��                         �                      �                         �                      �                        �                     �                         �                      �                         �                      �                         �                     �                        �               Q      5�_�       "           !          ����                                                                                                                                                                                                                                                                                                                                                             eR�     �             5��                          �              	       �                          �                     5�_�   !   #           "          ����                                                                                                                                                                                                                                                                                                                                                V       eR�9     �                   �             5��                          q                      �                          q                      5�_�   "   $           #          ����                                                                                                                                                                                                                                                                                                                                                V       eR�>     �                   form = GroupForm5��                         �                      5�_�   #   %           $          ����                                                                                                                                                                                                                                                                                                                                                V       eR�?     �                   form = GroupForm()5��                         �                      �       )                  �                      5�_�   $   &           %          ����                                                                                                                                                                                                                                                                                                                                                V       eR�J     �                    if request.method == "POST":5��                         �                      �       %                  �                      �       $                 �                     5�_�   %   '           &      1    ����                                                                                                                                                                                                                                                                                                                                                V       eR�P     �               2    if request.method == "POST" and form.is_valid:5��       1                  �                      5�_�   &   (           '      3    ����                                                                                                                                                                                                                                                                                                                                                V       eR�P     �               4    if request.method == "POST" and form.is_valid():5��       3                  �                      5�_�   '   )           (      )    ����                                                                                                                                                                                                                                                                                                                                                V       eR�S     �                *        # Get the group name from the form5��                          �       +               5�_�   (   *           )          ����                                                                                                                                                                                                                                                                                                                                                V       eR�X     �      	         3        group_name = request.POST.get('group_name')5��                        �                     �                         �                      �                        �                     5�_�   )   +           *      )    ����                                                                                                                                                                                                                                                                                                                                                V       eR�_     �      	         )        group_name = form.cleand_data.get5��       )                  �                      5�_�   *   ,           +      *    ����                                                                                                                                                                                                                                                                                                                                                V       eR�_     �      	         +        group_name = form.cleand_data.get()5��       *                  �                      5�_�   +               ,      +    ����                                                                                                                                                                                                                                                                                                                                                V       eR�`    �      	         -        group_name = form.cleand_data.get("")5��       +               
   �               
       5��