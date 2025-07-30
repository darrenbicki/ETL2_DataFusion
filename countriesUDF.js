function transformCSV(line) {
  // Skip header line
  if (line.startsWith("country_name,")) {
    return null; // skip header
  }

  // Split line by commas (simple CSV, no quotes handling)
  var values = line.split(',');

  var country_name = values[0];
  var capital = values[1];

  // Join remaining values in case languages contain commas
  var languagesRaw = values.slice(2).join(',');

  var languages = languagesRaw
    .split('|')
    .map(function(lang) { return lang.trim(); })
    .filter(function(lang) { return lang.length > 0; });

  var obj = {
    country_name: country_name,
    capital: capital,
    languages: languages
  };

  return JSON.stringify(obj);
}
