import requests

def get_quote():
    """
    Récupère une citation aléatoire depuis l'API ZenQuotes.

    L'API utilisée est ZenQuotes (https://zenquotes.io/).
    Si une erreur survient lors de la requête, un message d'erreur est retourné.

    Returns:
         La citation formatée avec son auteur, ou un message d'erreur.
    :rtype : str

    Exemple de retour :
        "The quote of the day is : 'Citation' - Auteur"
    """
    url = "https://zenquotes.io/api/random"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Vérifie si la requête est réussie
        quote_data = response.json()[0]
        return f'The quote of the day is : "{quote_data["q"]}" - {quote_data["a"]}'
    except requests.exceptions.RequestException as e:
        return f"Une erreur s'est produite : {e}"

if __name__ == "__main__":
    quote = get_quote()
    print(quote)