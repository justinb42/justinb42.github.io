---
title: ''
summary: ''
date: 2022-10-24
type: landing

design:
  spacing: '6rem'

sections:
  - block: resume-biography-3
    content:
      username: me
      text: ''
      button:
        text: Download CV
        url: uploads/bergfield-cv.pdf
      headings:
        about: ''
        education: ''
        interests: ''
    design:
      background:
        gradient_mesh:
          enable: true
      name:
        size: md
      avatar:
        size: large
        shape: rounded

  - block: markdown
    content:
      title: 'About the group'
      subtitle: ''
      text: |-
        We are a theory group in the Department of Physics at Illinois State University. We study
        systems where uniquely quantum resources, such as coherence, interference, and entanglement,
        can be used to overcome classical design challenges or avoid them entirely. We develop the
        theories and codes needed to investigate the entropy, charge, and spin transport through
        molecular junctions: open quantum systems composed of macroscopic electrodes coupled to
        microscopic molecules.

        These systems are ideal for investigating the interplay between strongly correlated matter,
        quantum nonequilibrium thermodynamics, and information theory, since quantum effects typically
        dominate a molecular junction's response, even at room temperature, and can be harnessed via
        molecular design or junction symmetry. The unifying question behind our projects is how
        information is encoded, observed, obscured, thermalized, and physically erased in quantum
        transport, and what each of those operations costs. See the [Research](/research/) page for
        the current program.

        The group includes M.S. and undergraduate students at ISU as well as high-school researchers,
        and we collaborate with experimental and theoretical groups elsewhere. Students interested in
        quantum transport, quantum thermodynamics, or scientific computing are welcome to get in touch.
    design:
      columns: '1'

  - block: collection
    id: papers
    content:
      title: Featured Publications
      filters:
        folders:
          - featured_publications
    design:
      view: article-grid
      columns: 2
---
