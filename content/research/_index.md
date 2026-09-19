---
title: Research
type: landing

sections:
  - block: markdown
    content:
      title: ""
      text: |
        <p class="lead">
        Quantum transport carries information not only in particle and energy currents, but also in
        <em>source memory</em>, <em>spectral correlations</em>, <em>coherent pathways</em>, and <em>spatial structure</em>.
        Our group develops thermoelectric probes to read that information, identifies the conditions under which
        it becomes inaccessible or irrelevant, and determines the thermodynamic resources required to erase or exploit it.
        </p>

        <p>
        The systems we study are molecular junctions and other open quantum conductors: microscopic, strongly
        quantum objects wired to macroscopic electrodes. Quantum effects dominate their response even at room
        temperature and can be tuned by molecular design and junction symmetry. We stay close to what can be
        measured: conductance, thermopower, heat current, local temperature, and light.
        Our work falls into four connected themes.
        </p>

        <ul class="theme-index">
          <li><a href="#manybody">1 · Many-body theory of quantum transport</a></li>
          <li><a href="#thermoelectrics">2 · Quantum-enhanced thermoelectrics</a></li>
          <li><a href="#cavity">3 · Cavity QED and transport</a></li>
          <li><a href="#information">4 · Quantum transport and information</a></li>
        </ul>

        <!-- ================================================================ -->
        <div class="research-theme" id="manybody">
          <div class="research-number">1</div>
          <h2>Many-body theory of quantum transport</h2>
          <p>
            The foundation of everything else we do. We develop nonequilibrium many-body theories of charge, heat,
            spin, and entropy flow through open quantum systems. The approach solves the few-body molecular problem
            exactly, including intramolecular interactions to all orders, and attaches macroscopic electrodes through a
            tunneling self-energy and a many-body Coulomb self-energy correction obtained from diagrammatic
            perturbation theory. The result is a Dyson-equation framework that connects microscopic electronic
            structure to measurable transport coefficients without giving up correlations or coherence.
          </p>
          <p>
            Within this framework we have asked what a local temperature or voltage <em>means</em> for a quantum
            system out of equilibrium, how many transmission channels a molecule really has, how Coulomb blockade and
            the Kondo effect appear in transport, and when Fourier's law of heat conduction emerges from
            quantum-coherent electrons. The last question has a surprisingly rich answer: atomically resolved
            temperature oscillations are physically present in a nanoscale conductor, finite spatial resolution washes
            them into a smooth profile, but true Fourier transport only emerges when many overlapping states
            contribute and interference self-averages.
          </p>
          <ul class="project-list">
            <li><strong>Many-body theory of single-molecule junctions.</strong> Exact few-body molecular Green's functions with electrode self-energies; the framework underlying our transport codes.</li>
            <li><strong>Local thermodynamic probes.</strong> Definitions and measurements of local temperature and voltage in nonequilibrium quantum systems, including thermoelectric corrections to quantum voltage measurement.</li>
            <li><strong>Emergence of Fourier's law.</strong> Heat-current vortices and fine structure in the resonant regime give way to laminar, resistor-network transport in the many-state limit.</li>
            <li><strong>Correlated transport.</strong> Coherent destruction of Coulomb-blockade peaks, the Kondo effect within density-functional theory, and many-body effects in molecular logic.</li>
          </ul>
          <div class="research-gallery">
            <figure>
              <img src="/media/research/bergfield_ratner_pssb_cover.jpg" alt="Journal cover on nonequilibrium heat and charge transport at the nanoscale.">
              <figcaption>Nonequilibrium heat and charge transport at the nanoscale.</figcaption>
            </figure>
          </div>
        </div>

        <!-- ================================================================ -->
        <div class="research-theme" id="thermoelectrics">
          <div class="research-number">2</div>
          <h2>Quantum-enhanced thermoelectrics</h2>
          <p>
            Thermopower measures the <em>energy dependence</em> of transmission rather than its magnitude, which makes
            it exquisitely sensitive to quantum interference. Near a transmission node created by destructive
            interference, thermopower can be enormous; near a higher-order "supernode," it can be enhanced further
            still, and the enhancement can be made to scale by connecting cross-conjugated units in series. We study
            how coherence, molecular symmetry, spin, and many-body effects push thermoelectric and spin-caloritronic
            response beyond classical expectations, and how the same sensitivity turns thermopower into a probe and
            an imaging tool.
          </p>
          <ul class="project-list">
            <li><strong>Supernodes and series-connected cross-conjugated junctions.</strong> Higher-order interference features as a route to scalable thermoelectric enhancement, and the role of dephasing in limiting it.</li>
            <li><strong>Spin-dependent thermoelectric response.</strong> Interference enhancement of the spin thermopower in single-molecule junctions.</li>
            <li><strong>Conductance–thermopower statistics.</strong> Identifying interference from the joint distribution of <em>G</em> and <em>S</em> in break-junction ensembles, and the robustness of thermopower to contact coupling. <span class="who">Makayla Dudley</span></li>
            <li><strong>Learning interference from transport statistics.</strong> Machine-learning classifiers that identify transmission nodes from synthetic break-junction data, benchmarked against analytic correlation rules. <span class="who">Sadhvik Paladugu, Sarayu Parsi, Dhruv Marlapaty</span></li>
            <li><strong>Scanning thermopower as a quantum-transport interferogram.</strong> A thermoelectric scanning probe that images interference structure directly. <span class="who">Helen Jilek</span></li>
            <li><strong>DNA nucleobase discrimination by thermopower.</strong> The same sensitivity applied to molecular identification in a transverse junction geometry. <span class="who">Helen Jilek</span></li>
          </ul>
          <div class="research-gallery">
            <figure>
              <img src="/media/research/thermopower.jpg" alt="Joint conductance–thermopower statistics revealing a quantum interference node.">
              <figcaption>Joint <em>G</em>–<em>S</em> statistics reveal interference that conductance alone cannot.</figcaption>
            </figure>
          </div>
        </div>

        <!-- ================================================================ -->
        <div class="research-theme" id="cavity">
          <div class="research-number">3</div>
          <h2>Cavity QED and transport</h2>
          <p>
            Information in a junction need not stay electronic. When a molecular junction sits inside an optical
            cavity or a plasmonic gap, its electronic states hybridize with light to form polaritons and plexcitons,
            and interference in the transport problem reshapes what the junction emits. We extend our many-body
            transport framework to include the cavity, so that electroluminescence, photon statistics, and transport
            can be treated on the same footing. Superconducting electrodes add correlated Cooper pairs as a further
            resource, with entanglement transfer between electronic and photonic degrees of freedom as the long-term
            target.
          </p>
          <ul class="project-list">
            <li><strong>Polaritonic states in molecular junctions.</strong> Cavity modes in the many-body Dyson framework, interference-enhanced light emission, and the dependence on cavity geometry. <span class="who">Joshua Klein</span></li>
            <li><strong>Plexcitonic signatures in electroluminescence.</strong> How strong coupling to a plasmonic gap shows up in the emitted light.</li>
            <li><strong>Superconducting molecular junctions.</strong> Non-classical light emission and symmetry-based design of quantum-enabled devices.</li>
          </ul>
        </div>

        <!-- ================================================================ -->
        <div class="research-theme" id="information">
          <div class="research-number">4</div>
          <h2>Quantum transport and information</h2>

          <div class="charter">
            <p class="charter-question">
              How is information encoded, observed, obscured, thermalized, and physically erased in quantum transport,
              and what are the thermodynamic consequences of each operation?
            </p>
          </div>

          <p>
            This is the question that ties the other three themes together and the focus of our current NSF award.
            "Quantum information" here does not mean importing qubits into molecular electronics. It means identifying
            the physically distinguishable structure encoded in an open quantum conductor, determining which
            measurements can recover it, and establishing what happens thermodynamically when it is hidden,
            thermalized, or removed.
          </p>

          <p>
            A molecular junction carries information at three levels, and our projects probe the maps between them.
            <strong>Structural information</strong> lives in the retarded Green's function and the contact matrices:
            which states exist, how they are connected, and the relative phases between paths. A transmission node is
            information of this kind; it records which-way distinguishability, and removing it means changing the
            Hilbert-space structure itself. <strong>Source information</strong> lives in the lesser Green's function:
            each electrode supplies a maximum-entropy Fermi distribution, but the molecule filters those streams
            coherently, so that carriers inside the junction still remember which reservoir they came from. Our 2013
            Maxwell's-demon paper resolved an apparent second-law paradox by exactly this memory. Finally, a local
            probe reports <strong>coarse-grained thermodynamic information</strong>: it replaces the whole structured
            distribution by two numbers, a local chemical potential and temperature, the maximum-entropy state
            consistent with what the probe can exchange. That projection is, quite literally, an erasure.
          </p>

          <p>
            Seen this way, several results that looked separate are witnesses of the same loss. Anomalous local
            temperatures and quantum corrections to Fourier's law both appear when a coherent nonequilibrium state is
            projected onto an information-poorer thermodynamic description, and both disappear when the missing
            information is physically erased or averaged away. Two of these
            operations look alike from the outside but are not: an observer with finite resolution can <em>fail to
            see</em> a quantum resource, which is not the same as the resource having been <em>erased</em>. Erasing
            structure in <em>G<sup>r</sup></em> and thermalizing populations in <em>G<sup>&lt;</sup></em> are different
            operations, and much of our work is about telling these cases apart.
          </p>

          <table class="ops-table">
            <thead>
              <tr><th>Operation</th><th>What changes</th><th>Status of the information</th><th>Where we study it</th></tr>
            </thead>
            <tbody>
              <tr><td><strong>Read</strong></td><td>the measurement channel</td><td>becomes experimentally accessible</td><td>scanning thermopower interferograms</td></tr>
              <tr><td><strong>Hide</strong></td><td>spatial or instrumental resolution</td><td>present but unresolved</td><td>coarse-grained temperature maps</td></tr>
              <tr><td><strong>Self-average</strong></td><td>number and overlap of contributing states</td><td>present microscopically, no longer controls transport</td><td>emergence of Fourier's law</td></tr>
              <tr><td><strong>Infer</strong></td><td>the choice of observables</td><td>only certain parameter combinations are identifiable</td><td>conductance–thermopower tomography</td></tr>
              <tr><td><strong>Thermalize</strong></td><td>distribution functions via probe constraints</td><td>reservoir and source memory discarded</td><td>voltage vs. voltage–temperature probes</td></tr>
              <tr><td><strong>Erase</strong></td><td>the retarded structure <em>G<sup>r</sup></em>, <em>Σ<sup>r</sup></em>, or contacts</td><td>an interference feature is physically removed</td><td>which-way information and erasure work</td></tr>
            </tbody>
          </table>

          <ul class="project-list">
            <li><strong>Which-way information and the cost of erasure.</strong> Treating the removal of an interference feature as a Landauer-type erasure with a minimum work cost.</li>
            <li><strong>Can local decoherence erase quantum interference?</strong> Thermodynamic consequences of the decoherence model, and the cost of erasing interference with local probes. <span class="who">Eren Erdoğan</span></li>
            <li><strong>Voltage vs. voltage–temperature probes.</strong> What a local probe measures depends on what it is allowed to equilibrate; comparing probe constraints isolates the information each one discards. <span class="who">Eren Erdoğan</span></li>
            <li><strong>Spin-resolved local probes.</strong> Probe thermometry extended to spin, as a local measure of which-path information near interference nodes. <span class="who">Vivaan Menon</span></li>
          </ul>
        </div>

        <div class="research-note">
          <p>
            <strong>Where this is going.</strong> Information in a junction is encoded, transported, made observable,
            inferred, coarse-grained, and erased, and something is discarded at every step. Our earlier work showed
            that electrons in a nanoscale conductor remember where they came from, and that this memory can be lost by
            resolution, by averaging, or by equilibration, each with different consequences. Our current work
            establishes how coherence and microscopic structure appear in electrical, thermoelectric, and optical
            observables. The next question is what those observables reveal, what physically removes that
            information, and what it costs, in work and entropy, to do so: what quantum coherence is worth, in joules.
            The applications follow from the same idea, in molecular imaging, thermoelectric characterization, DNA
            sequencing, and the controlled suppression of interference.
          </p>
        </div>

  - block: markdown
    content:
      title: ""
      text: |
        <div class="funding" id="funding">
          <h2>Funding</h2>
          <ul class="funding-list">
            <li>
              <span class="funding-agency">National Science Foundation</span>
              <a href="https://www.nsf.gov/awardsearch/showAward?AWD_ID=2412920" target="_blank" rel="noopener">RUI: Quantum Information of Interference Features in Transport</a>
              <span class="funding-meta">PHY, Award 2412920, 2024–2027</span>
            </li>
            <li>
              <span class="funding-agency">National Science Foundation</span>
              <a href="https://www.nsf.gov/awardsearch/showAward?AWD_ID=1809024" target="_blank" rel="noopener">RUI: Quantum Enhanced Thermoelectric Response of Molecule-based Systems</a>
              <span class="funding-meta">DMR, Award 1809024, 2019–2022</span>
            </li>
            <li>
              <span class="funding-agency">Air Force Research Laboratory</span>
              Six research awards for molecule-based material theory and design, quantum interference, and spin-dependent thermoelectric response
              <span class="funding-meta">Sensors Directorate, Wright-Patterson AFB, 2016–2020</span>
            </li>
            <li>
              <span class="funding-agency">Illinois State University</span>
              University Research Grant (2024); Pre-tenure Undergraduate Research Grants (2018, 2019)
            </li>
          </ul>
        </div>
---
