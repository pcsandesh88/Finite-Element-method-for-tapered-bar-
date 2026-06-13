# Finite-Element-method-for-tapered-bar
**Introduction**

A tapered bar is a structural member whose cross-sectional area varies along its length. Such members are commonly used in engineering applications where material optimization and weight reduction are important. Examples include transmission towers, aircraft components, crane booms, and machine elements. In this problem, a circular bar is subjected to an axial tensile load P, and its diameter decreases linearly from d 1 at the fixed end to d ,2 at the free end.  Because the diameter changes continuously, the cross-sectional area and stiffness also vary along the length of the bar. The objective is to determine the displacement of the free end using both the analytical method and the Finite Element Method (FEM).


**Axial Deformation of Bars**

When an axial force P acts on a bar, it produces normal stress and axial deformation.
Normal stress: σ= P/A
	​where:
σ = normal stress
P = axial load
A = cross-sectional area

According to Hooke's Law,
σ=Eϵ
where:
E = Young's modulus
ϵ = strain

Strain is defined as:
ϵ= dx/ du
Combining these equations:
dx/du = P/ (EA)
For a differential element:
du=P/(EA)dx
	
For a prismatic bar (constant area), total deformation is:
u= PL/EA However, for a tapered bar, the area varies with position, requiring integration along the length.

**Linear Diameter Variation**
The diameter changes linearly from d1 to d2 d(x)=d1+L(d2−d1)x
where:
x = distance from the fixed end
The area at any section becomes:
A(x)=π/4[d(x)]^2
Since area changes continuously, stiffness also changes continuously.

**Bar Element in FEM**

For a two-node bar element: Ke = EAe/le [1 −1 , -1 1 ]
where: ke = element stiffness matrix
Ae = element area
le = element length
E = Young's modulus

The element stiffness matrix relates nodal forces and nodal displacements.


**Global Stiffness Matrix**
After calculating the stiffness matrix of each element, all element matrices are assembled into a global stiffness matrix:
[K]{U}={F}
where:
[K] = global stiffness matrix
{U} = nodal displacement vector
{F} = external force vector

**Boundary Conditions**
For the tapered bar:
Fixed end:u1=0
Applied load at free end:Fn=P
After applying these conditions, the reduced matrix equation is solved for unknown nodal displacements.

**Conclusion**
The circular tapered bar is a non-prismatic member whose stiffness varies along its length because of the changing diameter. The analytical method provides an exact solution by integrating the deformation over the entire length. FEM provides an approximate numerical solution by dividing the bar into several uniform elements. Increasing the number of elements improves the accuracy of the FEM solution and causes it to converge toward the analytical result.
