---
title: ""
summary: ""
date: 2026-03-09
type: landing

sections:
  # 1. Carousel + tagline (Hihath-style)
  - block: markdown
    design:
      spacing:
        padding: ['2.5rem', '0', '2.5rem', '0']
    content:
      title: ""
      text: |
        <div class="home-tagline-block">
          <h1>Bergfield Research Group</h1>
          <p class="home-tagline">Reading the information hidden in quantum transport.</p>
          <p class="home-sub">Quantum transport theory · Department of Physics · Illinois State University</p>
        </div>
        {{< research-carousel >}}

  # 2. Mission
  - block: markdown
    design:
      spacing:
        padding: ['2.5rem', '0', '2.5rem', '0']
    content:
      title: ""
      text: |
        <div class="home-mission">
          <p class="lead">
          Quantum transport carries information not only in particle and energy currents, but also in
          source memory, spectral correlations, coherent pathways, and spatial structure. We develop
          thermoelectric probes to read that information, identify the conditions under which it becomes
          inaccessible or irrelevant, and determine the thermodynamic resources required to erase or exploit it.
          </p>
          <p class="plain">
          Put plainly: inside a molecule electrons behave like waves, and waves can cancel. Move the two contacts
          by a single atom and the current can vanish, not because anything blocks it, but because it cancels
          itself. Nature gives molecules their nearly perfect symmetry, and symmetry is what controls quantum
          behavior, so these effects survive at room temperature, in real environments, and in devices large
          enough to build. That is also what makes them useful: a fundamentally new way to switch current
          without heating, materials that convert waste heat or light into electricity, and a working laboratory
          for the physics of information itself.
          </p>
          <p>
          We are a theory group working on molecular junctions and other open quantum conductors, where quantum
          interference dominates the response even at room temperature. Our tools are nonequilibrium Green's
          functions, many-body Dyson-equation methods, and quantum thermodynamics; our observables are the ones
          experiments measure: conductance, thermopower, heat current, local temperature, and light.
          <a href="/research/">Learn more about our research →</a>
          </p>
        </div>

  # 3. Four research cards
  - block: markdown
    design:
      spacing:
        padding: ['2.5rem', '0', '2.5rem', '0']
    content:
      title: ""
      text: |
        <div class="research-cards">
          <a class="research-card" href="/research/#manybody">
            <img src="/media/research/multimode_benzene_pt.jpg" alt="A benzene molecule between two platinum electrodes">
            <div class="research-card-body">
              <div class="research-card-kicker">Theme 1</div>
              <h3>Many-body theory of quantum transport</h3>
              <p>Exact few-body molecular Green's functions, electrode self-energies, and what a local temperature means far from equilibrium.</p>
            </div>
          </a>
          <a class="research-card" href="/research/#thermoelectrics">
            <img src="/media/research/supernode_cross_conjugated.jpg" alt="A cross-conjugated molecule between gold electrodes">
            <div class="research-card-body">
              <div class="research-card-kicker">Theme 2</div>
              <h3>Quantum-enhanced thermoelectrics</h3>
              <p>Interference nodes and supernodes as a route to large thermopower, and thermopower as a probe and imaging tool.</p>
            </div>
          </a>
          <a class="research-card" href="/research/#cavity">
            <img src="/media/research/ppe_wire.jpg" alt="A polyphenylene ether wire between gold electrodes">
            <div class="research-card-body">
              <div class="research-card-kicker">Theme 3</div>
              <h3>Cavity QED and transport</h3>
              <p>Polaritons and plexcitons in molecular junctions; electroluminescence, photon statistics, and transport on one footing.</p>
            </div>
          </a>
          <a class="research-card" href="/research/#information">
            <img src="/media/research/maxwell_demon.jpg" alt="Maxwell's demon">
            <div class="research-card-body">
              <div class="research-card-kicker">Theme 4</div>
              <h3>Quantum transport and information</h3>
              <p>Interference as which-way information, decoherence as Landauer erasure, and what complete accounting restores a thermodynamic bound.</p>
            </div>
          </a>
        </div>

  # 4. Recent highlights
  - block: markdown
    design:
      spacing:
        padding: ['2.5rem', '0', '2.5rem', '0']
    content:
      title: ""
      text: |
        {{< newslist limit="5" >}}

  # 5. Featured publications
  - block: collection
    id: featured_publications
    content:
      title: Featured Publications
      filters:
        folders:
          - featured_publications
    design:
      spacing:
        padding: ['2.5rem', '0', '2.5rem', '0']
      view: article-grid
      columns: 2

  # 6. PI
  - block: markdown
    design:
      spacing:
        padding: ['2.5rem', '0', '2.5rem', '0']
    content:
      title: ""
      text: |
        <div class="home-pi">
          <div class="home-pi-text">
            <h2>Justin P. Bergfield</h2>
            <p class="home-pi-role">Professor of Physics, Illinois State University</p>
            <p>
            Justin investigates the quantum mechanical aspects of the flow of heat, charge, spin, and information
            at the nanoscale, with an emphasis on molecule-based systems. His work bridges condensed matter physics,
            chemistry, and electrical engineering.
            </p>
            <p>
            <a href="/about/">About →</a> &nbsp;·&nbsp;
            <a href="/members/">Group members →</a> &nbsp;·&nbsp;
            <a href="mailto:jpbergf@ilstu.edu">jpbergf@ilstu.edu</a> &nbsp;·&nbsp;
            <a href="https://scholar.google.com/citations?user=k2J0GZYAAAAJ" target="_blank" rel="noopener">Google Scholar</a>
            </p>
            <p class="home-funding">
            Supported by the National Science Foundation (PHY-2412920, DMR-1809024), the Air Force Research Laboratory, and Illinois State University.
            <a href="/research/#funding">Funding →</a>
            </p>
          </div>
        </div>
---
