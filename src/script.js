document.getElementById('calculator').addEventListener('submit', function(e) {
    e.preventDefault();
  
    const num1 = parseFloat(document.getElementById('num1').value);
    const num2 = parseFloat(document.getElementById('num2').value);
    const operation = document.getElementById('operation').value;
  
    let result;
  
    switch(operation) {
      case 'add':
        result = num1 + num2;
        break;
      case 'subtract':
        result = num1 - num2;
        break;
      case 'multiply':
        result = num1 * num2;
        break;
      case 'divide':
        if (num2 !== 0) {
          result = num1 / num2;
        } else {
          result = 'Erreur: Division par zéro';
        }
        break;
      default:
        result = 'Opération inconnue';
    }
  
    document.getElementById('result').textContent = `Résultat: ${result}`;
  });
  