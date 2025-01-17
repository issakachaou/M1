import tkinter as tk
from tkinter import messagebox
import pyperclip

def generate_email(mail_type, destinataire, entreprise=None, date=None, heure=None):
    debut = "Bonjour "
    fin = "\n\nRespectueusement,\nIssa Kachaou"

    if mail_type == "Réponse pour un mail d'étude de candidature":
        m1_1 = "Merci pour votre retour et pour l’attention portée à ma candidature.\n\nJe suis ravi à l’idée que mon profil puisse potentiellement contribuer aux ambitions de "
        m1_2 = "Je reste à votre disposition pour toute information complémentaire ou pour échanger lors d’un éventuel entretien.\n\nDans l’attente de votre retour, je vous remercie encore pour cette opportunité et vous souhaite une excellente journée."
        email_content = debut + destinataire + ",\n\n" + m1_1 + entreprise + ". " + m1_2 + fin

    elif mail_type == "Confirmation échange téléphonique":
        m2_1 = "Je vous remercie pour votre retour concernant ma candidature.\n\nJe vous confirme ma disponibilité pour un échange téléphonique "
        m2_2 = "Vous pourrez me joindre au 06 95 32 45 02 à l’heure convenue.\n\nDans l’attente de cet entretien, je reste à votre disposition si vous avez besoin d’informations complémentaires."
        email_content = debut + destinataire + ",\n\n" + m2_1 + date + " à " + heure + ". " + m2_2 + fin

    elif mail_type == "Confirmation entretien":
        m2_1 = "Je vous remercie pour votre retour concernant ma candidature.\n\nJe vous confirme ma disponibilité pour un entretien "
        m2_2 = "Vous pourrez me joindre au 06 95 32 45 02 à l’heure convenue.\n\nDans l’attente de cet entretien, je reste à votre disposition si vous avez besoin d’informations complémentaires."
        email_content = debut + destinataire + ",\n\n" + m2_1 + date + " à " + heure + ". " + m2_2 + fin

    elif mail_type == "Confirmation d'invitation teams":
        m3_1 = "Je vous confirme avoir bien reçu l’invitation Teams."
        m1_2 = "Je reste à votre disposition pour toute information complémentaire."
        email_content = debut + destinataire + ',\n\n' + m3_1 + '\n\n' + m1_2 + fin

    elif mail_type == "Avoir une justification pour un refus":
        m5_1 = "Je vous remercie pour votre retour concernant ma candidature."
        m5_2 = "Afin de m’améliorer dans mes futures démarches, je serais très reconnaissant si vous pouviez m’apporter quelques précisions sur les raisons de ce refus. Cela me permettrait de mieux comprendre les attentes de votre entreprise et de travailler sur les points nécessaires."
        m5_3 = "Je reste à votre disposition pour toute information complémentaire."
        email_content = debut + destinataire + ',\n\n' + m5_1 + '\n\n' + m5_2 + '\n\n' + m5_3 + fin

    # Afficher le contenu dans le cadre de sortie
    output_text.delete(1.0, tk.END)  # Effacer le texte précédent
    output_text.insert(tk.END, email_content)  # Insérer le nouveau contenu
    #pyperclip.copy(email_content)  # Copier le contenu dans le presse-papiers
    messagebox.showinfo("Email généré", "L'email a été copié dans le presse-papiers.")

# Création de la fenêtre principale
root = tk.Tk()
root.title("Générateur d'Email")

# Ajout des champs d'entrée
tk.Label(root, text="Type de mail:").grid(row=0, column=0)
mail_type_var = tk.StringVar(value="Type de Mail")
tk.OptionMenu(root, mail_type_var, "Réponse pour un mail d'étude de candidature", "Confirmation échange téléphonique", "Confirmation entretien", "Confirmation d'invitation teams", "Avoir une justification pour un refus").grid(row=0, column=1)

tk.Label(root, text="Destinataire:").grid(row=1, column=0)
destinataire_entry = tk.Entry(root)
destinataire_entry.grid(row=1, column=1)

tk.Label(root, text="Nom de l'entreprise:").grid(row=2, column=0)
entreprise_entry = tk.Entry(root)
entreprise_entry.grid(row=2, column=1)

tk.Label(root, text="Date:").grid(row=3, column=0)
date_entry = tk.Entry(root)
date_entry.grid(row=3, column=1)

tk.Label(root, text="Heure:").grid(row=4, column=0)
heure_entry = tk.Entry(root)
heure_entry.grid(row=4, column=1)

# Cadre de sortie pour afficher l'email
output_text = tk.Text(root, width=60, height=15) #60,15
output_text.grid(row=6, columnspan=2, padx=10, pady=10)

# Bouton pour générer l'email
generate_button = tk.Button(root, text="Générer Email", command=lambda: generate_email(
    mail_type_var.get(),
    destinataire_entry.get(),
    entreprise_entry.get(),
    date_entry.get(),
    heure_entry.get()
))
generate_button.grid(row=5, columnspan=2)

# Lancement de la boucle principale
root.mainloop()
