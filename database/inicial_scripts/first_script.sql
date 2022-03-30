SELECT * FROM users;

ALTER TABLE users MODIFY modified varchar(45) null;

INSERT INTO users (username, password, name, email, created, modified, isadmin) VALUES ('lgsouza', '222', 'Lucas Souza', 'lucasguellis.souza@gmail.com', now(), null, True);