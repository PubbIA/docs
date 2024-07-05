import streamlit as st



# Set the page configuration as the first Streamlit command
st.set_page_config(page_title="Boundif Poubelle Intelligent", page_icon="boundif.jpeg")

def main():
    st.title('Bienvenue à Boundif Poubelle Intelligent')
    st.markdown('### Membres de l\'équipe')
    st.write('- Ouail Laamiri')
    st.write('- Haddad Mohammed')
    st.write('- Ismail Oukha')

    st.markdown('### Présentation du Projet')
    st.write("Nous sommes une équipe passionnée participant au Hackathon ONCF 2024 avec notre projet 'Boundif Poubelle Intelligent'. Notre projet vise à révolutionner la gestion des déchets grâce à la technologie, en intégrant des fonctionnalités avancées pour améliorer l'engagement des utilisateurs, promouvoir la sensibilisation environnementale et rationaliser les efforts de recyclage.")

    st.markdown('### Fonctionnalités Clés')
    st.write('1. **Classification Automatique des Déchets** : Utilisation de la vision par ordinateur pour catégoriser automatiquement les types de déchets.')
    st.write('2. **Reconnaissance Faciale pour l\'Engagement Utilisateur** : Suivi personnalisé des utilisateurs et interactions gratifiantes.')
    st.write('3. **Système de Récompenses** : Points pour une élimination correcte des déchets, échangeables contre des incitations.')
    st.write('4. **Éducation Environnementale** : Conseils et conseils écologiques pour adopter des habitudes plus vertes.')
    st.write('5. **Interface de Recyclage** : Interface conviviale pour les recycleurs.')
    st.write('6. **Chatbot pour Idées de Recyclage** : Chatbot alimenté par l\'IA pour des idées de recyclage innovantes.')
    st.write('7. **Localisateur de Poubelles Intelligentes** : Localisez les poubelles intelligentes à proximité pour un élimination efficace.')


if __name__ == '__main__':
    main()
