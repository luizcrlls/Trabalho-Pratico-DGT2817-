def loginusuario(perfil):
    if perfil.lower() == "admin":
        print("Bem vindo, Administrador")
    else:
        print("Bem vindo, Usuario")
loginusuario("Admin")
loginusuario("admin")
loginusuario("user")
loginusuario("Usuario")
