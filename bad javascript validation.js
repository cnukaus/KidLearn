<if <%passwd_retrieved_fromserver%> == user_typed_pass
then
// validated
else
endif>


<if user_typed == local_stored_var

oauth2.0 了解下。前端每次访问非开放接口都要加上 token。后端会验证是否过期，和权限信息。我一般会把Id name 都存进去。。。。一般业务场景这个2个对象够用了

你这算什么，我大学时教务网登录校验就是把密码取出用js比对，随便输入密码，再查看源码就能看到真实密码了。这逻辑简直就是用屁股想出来的，网站是东软做的