#! /bin/bash
composer install
npm i
cp .env.example .env
vim .env
php artisan key:generate
php artisan migrate:fresh --seed
npm run build
cp artisan art
chmod +x art
./art serve
