# Feature: Hotel Inventory Management

## Description
This module handles the core inventory elements for a hotel management system, primarily focusing on Room Types, Rooms, and Amenities.

## Business Requirements
1. **Room Types**: The system must track different categories of rooms (e.g., Standard, Deluxe, Suite). Each type should define a base price and a maximum occupancy limit.
2. **Rooms**: Every physical room must have a unique identifier (Room Number), a status (Available, Occupied, Maintenance), and an assigned Room Type.
3. **Amenities**: Rooms can have associated amenities (e.g., Ocean View, Balcony, Minibar). These amenities might affect the final pricing.

## Acceptance Criteria
- As an admin, I can create and manage Room Types, including their descriptions and base rates.
- As an admin, I can add new Rooms and assign them to a specific Room Type.
- The system prevents assigning a room to a non-existent Room Type.
- Tests should verify that a Room cannot be 'Available' while also being assigned to an active Booking (booking logic will be in another spec, but tests should reflect the status constraint).
