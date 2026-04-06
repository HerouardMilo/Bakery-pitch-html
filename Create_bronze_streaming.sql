CREATE TABLE IF NOT EXISTS bronze_streaming (
    id_vente VARCHAR,
    id_produit VARCHAR,
    quantite INTEGER,
    prix_unitaire_ttc DOUBLE,
    total_ligne_ttc DOUBLE,
    remise_pct DOUBLE,
    sur_place BOOLEAN,
    id_client VARCHAR,
    type_reglement VARCHAR,
    timestamp VARCHAR,
    loaded_at VARCHAR
);
