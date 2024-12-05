-- Création de la base de données
CREATE DATABASE IF NOT EXISTS DET;
USE DET;

-- Création de la table bsi
CREATE TABLE bsi (
    blood_type ENUM('O-', 'O+', 'B-', 'B+', 'A-', 'A+', 'AB-', 'AB+') NOT NULL, -- Groupe sanguin
    rarity_level ENUM('common', 'rare', 'very_rare') NOT NULL,                 -- Niveau de rareté
    quantity INT NOT NULL                                                     -- Quantité en stock
);

-- Insertion des données dans la table bsi
INSERT INTO bsi (blood_type, rarity_level, quantity)
VALUES
    ('O-', 'rare', 40),
    ('O+', 'common', 100),
    ('B-', 'rare', 20),
    ('B+', 'common', 50),
    ('A-', 'rare', 30),
    ('A+', 'common', 80),
    ('AB-', 'very_rare', 10),
    ('AB+', 'rare', 15);

-- Requête pour afficher toutes les données de la table bsi
SELECT * FROM bsi;