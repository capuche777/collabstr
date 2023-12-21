async function getSection(sectName) {
  const response = await fetch(`/users/?search=${sectName}`)
  return await response.json()
}


const createDOM = function (secName, data) {
  let mainSect = document.getElementsByClassName('all')[0]
  let colPerRow = 4
  let totalRows = data.length / colPerRow
  let section = document.getElementById(secName)

  mainSect.classList.add('d-none')
  section.innerHTML = ''

  let dividedData = []

  let start = 0
  let end = start + 4

  for ( let i = 0; i < data.length; i++) {
    // creating sub arrays to work better with data
    if (i < totalRows ) {
      dividedData.push(data.slice(start, end))
      start = end+1
      end = start + 4
    }
  }

  dividedData.forEach(function (v, i) {
    section.innerHTML += `<div class="row pt-3 pb-5 dynamic-row"></div>`

    for (let j = 0; j < v.length; j++) {



      if (v[j]['content']['url'].split('.')[3] === 'webp') {
        document.getElementsByClassName('dynamic-row')[i].innerHTML += `
        <div class="col-md-3">
            <div class="card"><img src="${v[j]['content']['url']}" ></div>
            <div class="d-table-cell">
                <p class="fw-light m-0">${v[j]['username']}</p>
                <p class="fw-light m-0">${v[j]['first_name']}</p>
            </div>
            <div class="d-table-cell text-end">
                <p class="m-0">Rating: ${parseInt(v[j]['creator']['rating'])} <i class="fas fa-star text-warning"></i></p>
                <a href="${v[j]['content']['url']}"><i class="fas fa-download text-success"></i></a>
            </div>
        </div>
      `
      } else  {
        document.getElementsByClassName('dynamic-row')[i].innerHTML += `
        <div class="col-md-3">
            <div class="card">
            <video width="100%" height="315" loop muted controls type="video/mp4">
                <source src="${v[j]['content']['url']}">
            </video>
            <div class="d-table-cell">
                <p class="fw-light m-0">${v[j]['username']}</p>
                <p class="fw-light m-0">${v[j]['first_name']}</p>
            </div>
            <div class="d-table-cell text-end">
                <p class="m-0">Rating: ${parseInt(v[j]['creator']['rating'])} <i class="fas fa-star text-warning"></i></p>
                <a href="${v[j]['content']['url']}"><i class="fas fa-download text-success"></i></a>
            </div>
        </div>
      `
      }
    }
  })

}


document.querySelectorAll('[role="tab"]').forEach(function (el) {
  el.onclick = function (){
    let sectName = el.textContent

    if ( sectName !== 'All') {
      getSection(sectName).then(
        res => {
          createDOM(sectName.replace(/\s+/g, '-').toLocaleLowerCase(), res)
        }
      )
    } else {
      document.getElementsByClassName('all')[0].classList.remove('d-none')
    }
  }
})
