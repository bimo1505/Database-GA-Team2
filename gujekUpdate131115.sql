--
-- PostgreSQL database dump
--

SET statement_timeout = 0;
SET lock_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SET check_function_bodies = false;
SET client_min_messages = warning;

--
-- Name: ASG_DB; Type: COMMENT; Schema: -; Owner: postgres
--

COMMENT ON DATABASE "ASG_DB" IS 'This is the database for the database group assignment.';


--
-- Name: gujek; Type: SCHEMA; Schema: -; Owner: postgres
--

CREATE SCHEMA gujek;


ALTER SCHEMA gujek OWNER TO postgres;

--
-- Name: plpgsql; Type: EXTENSION; Schema: -; Owner: 
--

CREATE EXTENSION IF NOT EXISTS plpgsql WITH SCHEMA pg_catalog;


--
-- Name: EXTENSION plpgsql; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION plpgsql IS 'PL/pgSQL procedural language';


SET search_path = gujek, pg_catalog;

SET default_tablespace = '';

SET default_with_oids = false;

--
-- Name: analyst; Type: TABLE; Schema: gujek; Owner: postgres; Tablespace: 
--

CREATE TABLE analyst (
    id character(10) NOT NULL
);


ALTER TABLE analyst OWNER TO postgres;

--
-- Name: app; Type: TABLE; Schema: gujek; Owner: postgres; Tablespace: 
--

CREATE TABLE app (
    version character varying(5) NOT NULL,
    date date NOT NULL
);


ALTER TABLE app OWNER TO postgres;

--
-- Name: app_design_team; Type: TABLE; Schema: gujek; Owner: postgres; Tablespace: 
--

CREATE TABLE app_design_team (
    member_id character(10) NOT NULL,
    education character varying(3) NOT NULL,
    email character varying(40) NOT NULL
);


ALTER TABLE app_design_team OWNER TO postgres;

--
-- Name: customer; Type: TABLE; Schema: gujek; Owner: postgres; Tablespace: 
--

CREATE TABLE customer (
    customer_number character(10) NOT NULL,
    name character varying(30) NOT NULL,
    email character varying(30) NOT NULL,
    username character varying(30) NOT NULL,
    password character varying(32) NOT NULL,
    phone_number character varying(15) NOT NULL
);


ALTER TABLE customer OWNER TO postgres;

--
-- Name: delivery; Type: TABLE; Schema: gujek; Owner: postgres; Tablespace: 
--

CREATE TABLE delivery (
    transaction_number character(10) NOT NULL,
    "time" timestamp with time zone NOT NULL,
    goods character varying(40) NOT NULL
);


ALTER TABLE delivery OWNER TO postgres;

--
-- Name: driver; Type: TABLE; Schema: gujek; Owner: postgres; Tablespace: 
--

CREATE TABLE driver (
    id character(10) NOT NULL
);


ALTER TABLE driver OWNER TO postgres;

--
-- Name: employee; Type: TABLE; Schema: gujek; Owner: postgres; Tablespace: 
--

CREATE TABLE employee (
    id character(10) NOT NULL,
    supervisor_id character(10),
    name character varying(30),
    birth_date date,
    gender character varying(6),
    address character varying(30),
    phone character varying(15)
);


ALTER TABLE employee OWNER TO postgres;

--
-- Name: feedback; Type: TABLE; Schema: gujek; Owner: postgres; Tablespace: 
--

CREATE TABLE feedback (
    customer_number character(10) NOT NULL,
    version character varying(5) NOT NULL,
    date date NOT NULL,
    rate integer NOT NULL,
    comment text
);


ALTER TABLE feedback OWNER TO postgres;

--
-- Name: food; Type: TABLE; Schema: gujek; Owner: postgres; Tablespace: 
--

CREATE TABLE food (
    transaction_number character(10) NOT NULL,
    "time" timestamp with time zone NOT NULL,
    resto_name character varying(40) NOT NULL
);


ALTER TABLE food OWNER TO postgres;

--
-- Name: restaurant; Type: TABLE; Schema: gujek; Owner: postgres; Tablespace: 
--

CREATE TABLE restaurant (
    name character varying(30) NOT NULL,
    menu text NOT NULL,
    price integer NOT NULL,
    address character varying(40) NOT NULL,
    phone_number character varying(15) NOT NULL
);


ALTER TABLE restaurant OWNER TO postgres;

--
-- Name: software_engineer; Type: TABLE; Schema: gujek; Owner: postgres; Tablespace: 
--

CREATE TABLE software_engineer (
    id character(10) NOT NULL
);


ALTER TABLE software_engineer OWNER TO postgres;

--
-- Name: supervisor; Type: TABLE; Schema: gujek; Owner: postgres; Tablespace: 
--

CREATE TABLE supervisor (
    id character(10) NOT NULL,
    email character varying(30) NOT NULL
);


ALTER TABLE supervisor OWNER TO postgres;

--
-- Name: taxi; Type: TABLE; Schema: gujek; Owner: postgres; Tablespace: 
--

CREATE TABLE taxi (
    transaction_number character(10) NOT NULL,
    "time" timestamp with time zone NOT NULL,
    destination character varying(40) NOT NULL
);


ALTER TABLE taxi OWNER TO postgres;

--
-- Name: transaction; Type: TABLE; Schema: gujek; Owner: postgres; Tablespace: 
--

CREATE TABLE transaction (
    transaction_number character(10) NOT NULL,
    "time" timestamp with time zone NOT NULL,
    driver_id character(10) NOT NULL,
    customer_number character(10) NOT NULL
);


ALTER TABLE transaction OWNER TO postgres;

--
-- Name: vehicle; Type: TABLE; Schema: gujek; Owner: postgres; Tablespace: 
--

CREATE TABLE vehicle (
    license character(13) NOT NULL,
    driver_id character(10) NOT NULL,
    type character varying(10) NOT NULL,
    years character(4) NOT NULL
);


ALTER TABLE vehicle OWNER TO postgres;

--
-- Name: works_on; Type: TABLE; Schema: gujek; Owner: postgres; Tablespace: 
--

CREATE TABLE works_on (
    member_id character(10) NOT NULL,
    version character varying(5) NOT NULL,
    date date NOT NULL
);


ALTER TABLE works_on OWNER TO postgres;

--
-- Data for Name: analyst; Type: TABLE DATA; Schema: gujek; Owner: postgres
--

COPY analyst (id) FROM stdin;
1406600001
1406600004
\.


--
-- Data for Name: app; Type: TABLE DATA; Schema: gujek; Owner: postgres
--

COPY app (version, date) FROM stdin;
1.01	2014-12-10
1.02	2015-09-09
\.


--
-- Data for Name: app_design_team; Type: TABLE DATA; Schema: gujek; Owner: postgres
--

COPY app_design_team (member_id, education, email) FROM stdin;
1406600001	S3	agazsi.n@hotmail.com
1406600004	S1	fav@ui.ac.id
1406600005	S1	Mets@ui.ac.id
\.


--
-- Data for Name: customer; Type: TABLE DATA; Schema: gujek; Owner: postgres
--

COPY customer (customer_number, name, email, username, password, phone_number) FROM stdin;
66602     	James Hunt	hunt@ui.ac.id	james.hunt	09281	081222199928
66603     	Candice	candice@chilli.com	candice.s	12348	0813991262811
66601     	Yanuar Chilli	imchilli@hotmail.com	imachilli123	12345	08139991099
\.


--
-- Data for Name: delivery; Type: TABLE DATA; Schema: gujek; Owner: postgres
--

COPY delivery (transaction_number, "time", goods) FROM stdin;
44401     	2015-03-03 12:45:30+07	Baju-baju 
44403     	2015-03-07 02:43:22+07	CPU
\.


--
-- Data for Name: driver; Type: TABLE DATA; Schema: gujek; Owner: postgres
--

COPY driver (id) FROM stdin;
1406600003
1406600006
\.


--
-- Data for Name: employee; Type: TABLE DATA; Schema: gujek; Owner: postgres
--

COPY employee (id, supervisor_id, name, birth_date, gender, address, phone) FROM stdin;
1406600003	1406600001	Revin	1996-04-20	M	Jl. Neraka jahanam	0813666666666
1406600004	1406600002	Favian 	1996-02-10	M	Jl. Lebak lestari timur	0832477234932
1406600005	1406600001	Meta	1996-04-15	W	Jl. Bintaro sektor 1	081392728291
1406600006	1406600002	Ricky 	1996-10-11	M	Jl. Kira utara	08139182972
1406600001	1406600003	Agazsi N. Bahasoean	1995-07-07	M	Jl. Brawijaya 8 no 12	08139172917
1406600002	1406600003	Bimo Prabowo	1995-02-03	M	Jl. Karang asem tengah	082393739283
null      	\N	\N	\N	\N	\N	\N
\.


--
-- Data for Name: feedback; Type: TABLE DATA; Schema: gujek; Owner: postgres
--

COPY feedback (customer_number, version, date, rate, comment) FROM stdin;
66601     	1.01	2014-12-10	8	im in love with it 
66603     	1.01	2014-12-10	7	pretty good yes
\.


--
-- Data for Name: food; Type: TABLE DATA; Schema: gujek; Owner: postgres
--

COPY food (transaction_number, "time", resto_name) FROM stdin;
44404     	2015-03-25 11:30:10+07	Ayam MAS MONO
\.


--
-- Data for Name: restaurant; Type: TABLE DATA; Schema: gujek; Owner: postgres
--

COPY restaurant (name, menu, price, address, phone_number) FROM stdin;
Ayam MAS MONO	ayam spesial mas mono	40	Jl. Kemang raya utara blok C 11	75839809
Nasi padang cabai pedas	nasi goreng	20	Jl. Kalimalang 8 jakarta utara	7812312
Bebek Haji Slamet	bebek	30	Jl. Lebak  lestari 2 Jakarta Selatan	7827191
\.


--
-- Data for Name: software_engineer; Type: TABLE DATA; Schema: gujek; Owner: postgres
--

COPY software_engineer (id) FROM stdin;
1406600001
1406600004
\.


--
-- Data for Name: supervisor; Type: TABLE DATA; Schema: gujek; Owner: postgres
--

COPY supervisor (id, email) FROM stdin;
1406600001	agazsi.n@hotmail.com
1406600002	bimo.p@ui.ac.id
null      	null
1406600003	NULL
\.


--
-- Data for Name: taxi; Type: TABLE DATA; Schema: gujek; Owner: postgres
--

COPY taxi (transaction_number, "time", destination) FROM stdin;
44402     	2015-03-05 01:30:10+07	Senayan City
\.


--
-- Data for Name: transaction; Type: TABLE DATA; Schema: gujek; Owner: postgres
--

COPY transaction (transaction_number, "time", driver_id, customer_number) FROM stdin;
44401     	2015-03-03 12:45:30+07	1406600003	66601     
44402     	2015-03-05 01:30:10+07	1406600006	66602     
44403     	2015-03-07 02:43:22+07	1406600006	66603     
44404     	2015-03-25 11:30:10+07	1406600003	66602     
\.


--
-- Data for Name: vehicle; Type: TABLE DATA; Schema: gujek; Owner: postgres
--

COPY vehicle (license, driver_id, type, years) FROM stdin;
B7070SZ      	1406600003	motor	2007
B1234SC      	1406600006	motor	2008
\.


--
-- Data for Name: works_on; Type: TABLE DATA; Schema: gujek; Owner: postgres
--

COPY works_on (member_id, version, date) FROM stdin;
1406600001	1.02	2015-09-09
1406600004	1.02	2015-09-09
1406600005	1.02	2015-09-09
\.


--
-- Name: APP_PKEY; Type: CONSTRAINT; Schema: gujek; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY app
    ADD CONSTRAINT "APP_PKEY" PRIMARY KEY (version, date);


--
-- Name: VEHICLE_PKEY; Type: CONSTRAINT; Schema: gujek; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY vehicle
    ADD CONSTRAINT "VEHICLE_PKEY" PRIMARY KEY (license, driver_id);


--
-- Name: WORKS_ON_PKEY; Type: CONSTRAINT; Schema: gujek; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY works_on
    ADD CONSTRAINT "WORKS_ON_PKEY" PRIMARY KEY (member_id, version, date);


--
-- Name: analyst_pkey; Type: CONSTRAINT; Schema: gujek; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY analyst
    ADD CONSTRAINT analyst_pkey PRIMARY KEY (id);


--
-- Name: app_design_team_pkey; Type: CONSTRAINT; Schema: gujek; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY app_design_team
    ADD CONSTRAINT app_design_team_pkey PRIMARY KEY (member_id);


--
-- Name: customer_pkey; Type: CONSTRAINT; Schema: gujek; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY customer
    ADD CONSTRAINT customer_pkey PRIMARY KEY (customer_number);


--
-- Name: delivery_pkey; Type: CONSTRAINT; Schema: gujek; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY delivery
    ADD CONSTRAINT delivery_pkey PRIMARY KEY (transaction_number, "time");


--
-- Name: driver_pkey; Type: CONSTRAINT; Schema: gujek; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY driver
    ADD CONSTRAINT driver_pkey PRIMARY KEY (id);


--
-- Name: employee_pkey; Type: CONSTRAINT; Schema: gujek; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY employee
    ADD CONSTRAINT employee_pkey PRIMARY KEY (id);


--
-- Name: feedback_pkey; Type: CONSTRAINT; Schema: gujek; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY feedback
    ADD CONSTRAINT feedback_pkey PRIMARY KEY (customer_number, version, date);


--
-- Name: food_pkey; Type: CONSTRAINT; Schema: gujek; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY food
    ADD CONSTRAINT food_pkey PRIMARY KEY (transaction_number, "time", resto_name);


--
-- Name: restaurant_pkey; Type: CONSTRAINT; Schema: gujek; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY restaurant
    ADD CONSTRAINT restaurant_pkey PRIMARY KEY (name);


--
-- Name: software_engineer_pkey; Type: CONSTRAINT; Schema: gujek; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY software_engineer
    ADD CONSTRAINT software_engineer_pkey PRIMARY KEY (id);


--
-- Name: supervisor_pkey; Type: CONSTRAINT; Schema: gujek; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY supervisor
    ADD CONSTRAINT supervisor_pkey PRIMARY KEY (id);


--
-- Name: taxi_pkey; Type: CONSTRAINT; Schema: gujek; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY taxi
    ADD CONSTRAINT taxi_pkey PRIMARY KEY (transaction_number, "time");


--
-- Name: transaction_pkey; Type: CONSTRAINT; Schema: gujek; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY transaction
    ADD CONSTRAINT transaction_pkey PRIMARY KEY (transaction_number, "time");


--
-- Name: analyst_id_fkey; Type: FK CONSTRAINT; Schema: gujek; Owner: postgres
--

ALTER TABLE ONLY analyst
    ADD CONSTRAINT analyst_id_fkey FOREIGN KEY (id) REFERENCES employee(id);


--
-- Name: analyst_id_fkey1; Type: FK CONSTRAINT; Schema: gujek; Owner: postgres
--

ALTER TABLE ONLY analyst
    ADD CONSTRAINT analyst_id_fkey1 FOREIGN KEY (id) REFERENCES app_design_team(member_id);


--
-- Name: delivery_transaction_number_fkey; Type: FK CONSTRAINT; Schema: gujek; Owner: postgres
--

ALTER TABLE ONLY delivery
    ADD CONSTRAINT delivery_transaction_number_fkey FOREIGN KEY (transaction_number, "time") REFERENCES transaction(transaction_number, "time");


--
-- Name: driver_id_fkey; Type: FK CONSTRAINT; Schema: gujek; Owner: postgres
--

ALTER TABLE ONLY driver
    ADD CONSTRAINT driver_id_fkey FOREIGN KEY (id) REFERENCES employee(id);


--
-- Name: employee_supervisor_id_fkey; Type: FK CONSTRAINT; Schema: gujek; Owner: postgres
--

ALTER TABLE ONLY employee
    ADD CONSTRAINT employee_supervisor_id_fkey FOREIGN KEY (supervisor_id) REFERENCES supervisor(id);


--
-- Name: feedback_customer_number_fkey; Type: FK CONSTRAINT; Schema: gujek; Owner: postgres
--

ALTER TABLE ONLY feedback
    ADD CONSTRAINT feedback_customer_number_fkey FOREIGN KEY (customer_number) REFERENCES customer(customer_number);


--
-- Name: feedback_version_fkey; Type: FK CONSTRAINT; Schema: gujek; Owner: postgres
--

ALTER TABLE ONLY feedback
    ADD CONSTRAINT feedback_version_fkey FOREIGN KEY (version, date) REFERENCES app(version, date);


--
-- Name: food_resto_name_fkey; Type: FK CONSTRAINT; Schema: gujek; Owner: postgres
--

ALTER TABLE ONLY food
    ADD CONSTRAINT food_resto_name_fkey FOREIGN KEY (resto_name) REFERENCES restaurant(name);


--
-- Name: food_transaction_number_fkey; Type: FK CONSTRAINT; Schema: gujek; Owner: postgres
--

ALTER TABLE ONLY food
    ADD CONSTRAINT food_transaction_number_fkey FOREIGN KEY (transaction_number, "time") REFERENCES transaction(transaction_number, "time");


--
-- Name: software_engineer_id_fkey; Type: FK CONSTRAINT; Schema: gujek; Owner: postgres
--

ALTER TABLE ONLY software_engineer
    ADD CONSTRAINT software_engineer_id_fkey FOREIGN KEY (id) REFERENCES employee(id);


--
-- Name: software_engineer_id_fkey1; Type: FK CONSTRAINT; Schema: gujek; Owner: postgres
--

ALTER TABLE ONLY software_engineer
    ADD CONSTRAINT software_engineer_id_fkey1 FOREIGN KEY (id) REFERENCES app_design_team(member_id);


--
-- Name: supervisor_id_fkey; Type: FK CONSTRAINT; Schema: gujek; Owner: postgres
--

ALTER TABLE ONLY supervisor
    ADD CONSTRAINT supervisor_id_fkey FOREIGN KEY (id) REFERENCES employee(id);


--
-- Name: taxi_transaction_number_fkey; Type: FK CONSTRAINT; Schema: gujek; Owner: postgres
--

ALTER TABLE ONLY taxi
    ADD CONSTRAINT taxi_transaction_number_fkey FOREIGN KEY (transaction_number, "time") REFERENCES transaction(transaction_number, "time");


--
-- Name: transaction_customer_number_fkey; Type: FK CONSTRAINT; Schema: gujek; Owner: postgres
--

ALTER TABLE ONLY transaction
    ADD CONSTRAINT transaction_customer_number_fkey FOREIGN KEY (customer_number) REFERENCES customer(customer_number);


--
-- Name: transaction_driver_id_fkey; Type: FK CONSTRAINT; Schema: gujek; Owner: postgres
--

ALTER TABLE ONLY transaction
    ADD CONSTRAINT transaction_driver_id_fkey FOREIGN KEY (driver_id) REFERENCES driver(id);


--
-- Name: vehicle_driver_id_fkey; Type: FK CONSTRAINT; Schema: gujek; Owner: postgres
--

ALTER TABLE ONLY vehicle
    ADD CONSTRAINT vehicle_driver_id_fkey FOREIGN KEY (driver_id) REFERENCES driver(id);


--
-- Name: works_on_member_id_fkey; Type: FK CONSTRAINT; Schema: gujek; Owner: postgres
--

ALTER TABLE ONLY works_on
    ADD CONSTRAINT works_on_member_id_fkey FOREIGN KEY (member_id) REFERENCES app_design_team(member_id);


--
-- Name: works_on_version_fkey; Type: FK CONSTRAINT; Schema: gujek; Owner: postgres
--

ALTER TABLE ONLY works_on
    ADD CONSTRAINT works_on_version_fkey FOREIGN KEY (version, date) REFERENCES app(version, date);


--
-- Name: public; Type: ACL; Schema: -; Owner: postgres
--

REVOKE ALL ON SCHEMA public FROM PUBLIC;
REVOKE ALL ON SCHEMA public FROM postgres;
GRANT ALL ON SCHEMA public TO postgres;
GRANT ALL ON SCHEMA public TO PUBLIC;


--
-- PostgreSQL database dump complete
--

