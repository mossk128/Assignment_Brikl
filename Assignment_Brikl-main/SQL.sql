CREATE TABLE products (
  id INT PRIMARY KEY,
  title VARCHAR(255),
  description TEXT,
  price FLOAT,
  available_date TIMESTAMP,
  stock_quantity INT,
  images TEXT,
  category VARCHAR(255)
);

CREATE TABLE storefronts (
  id INT PRIMARY KEY,
  name VARCHAR(255),
  user_id INT, -- foreign key to users table
  -- other columns specific to storefronts
);

CREATE TABLE microstores (
  id INT PRIMARY KEY,
  name VARCHAR(255),
  user_id INT, -- foreign key to users table
  -- other columns specific to microstores
);

CREATE TABLE promotional_products (
  microstore_id INT, -- foreign key to microstores table
  product_id INT, -- foreign key to products table
  PRIMARY KEY (microstore_id, product_id)
);

CREATE TABLE storefront_products (
  storefront_id INT, -- foreign key to storefronts table
  product_id INT, -- foreign key to products table
  PRIMARY KEY (storefront_id, product_id)
);
