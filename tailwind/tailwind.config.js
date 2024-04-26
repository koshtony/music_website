/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["../**/*.html", "./node_modules/flowbite/**/*.js"],
  theme: {
    extend: {
      backgroundImage: {
        'ticketSectionBgImage': "url('../src/static/img/c-1.jpg')",
      }
    },
  },
  plugins: [
    require('flowbite/plugin')
  ],
}

