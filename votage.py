from blessed import Terminal
term = Terminal()


nom = input("Votre nom et nom de famille: ")
candidat1 = "Nathaniel"
candidat2 = "Felix"
candidat3 = "Zakaria"
candidats = [candidat1, candidat2, candidat3]
# print(f"Choix candidats: {candidat1}, {candidat2} et {candidat3}")


def render(choix_possibles):
    selected_option = 0
    with term.cbreak(), term.hidden_cursor():
        while True:
            with term.location(y=(term.height // 2) - 5):
                # Highlight le choix choisi
                for i, choix in enumerate(choix_possibles):
                    if i == selected_option:
                        # Highlight l'option selectionee
                        print(term.center(term.reverse(f"> {choix} <")))
                    else:
                        # Imprime normalement les autres options
                        print(term.center(f"  {choix}  "))

                # Input du joueur
            key = term.inkey(timeout=0.5)
            if key.code == term.KEY_UP:  # Quand touche enregistree est KEY_UP: Changer d'option vers le haut
                selected_option = (selected_option - 1) % len(choix_possibles)
            elif key.code == term.KEY_DOWN:  # Quand touche enregistree est KEY_DOWN: Changer d'option vers le bas
                selected_option = (selected_option + 1) % len(choix_possibles)
            elif key.code == term.KEY_ENTER:  # Quand touche ENTER: Regarde l'option selectionnee
                if selected_option == 0:
                    return
                elif selected_option == 1:
                    return
                elif selected_option == 2:
                    return
                
render(candidats)