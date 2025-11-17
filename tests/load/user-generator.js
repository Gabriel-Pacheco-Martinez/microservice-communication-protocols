module.exports = {
  // Generate a random alphanumeric string (length 8)
  randomString: function () {
    return Math.random().toString(36).substring(2, 10);
  },

  // Random string followed by @gmail.com
  randomEmail: function () {
    return Math.random().toString(36).substring(2, 10) + "@gmail.com";
  }
};